from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# If clean_data.py renamed columns (P18), change ONLY these values
DATE, REV, PROFIT = "Order_Date", "Net_Revenue_INR", "Profit_INR"
PRODUCT, REGION, CITY, CHANNEL = "Product_Name", "Region", "City", "Sales_Channel"
DISC, QTY, RATING = "Discount_Pct", "Quantity", "Customer_Rating"


def run_visualization(df, report_dir):
  charts = Path(report_dir) / "charts"
  charts.mkdir(parents=True, exist_ok=True)

  df = df.copy()
  df[DATE] = pd.to_datetime(df[DATE])
  df["Month"] = df[DATE].dt.to_period("M").dt.to_timestamp()
  df["Quarter"] = "Q" + df[DATE].dt.quarter.astype(str)
  df["Margin"] = np.where(df[REV] > 0, df[PROFIT] / df[REV] * 100, np.nan)

  insights = []

  def save(name, text):
      plt.tight_layout()
      plt.savefig(charts / f"{name}.png", dpi=150)
      plt.close()
      insights.append(f"{name}: {text}")

  # V01
  m = df.groupby("Month")[REV].sum()
  plt.figure(figsize=(10, 5))
  plt.plot(m.index, m.values, marker="o", label="Net Revenue")
  plt.title("Monthly Net Revenue (2025)")
  plt.xlabel("Month"); plt.ylabel("Net Revenue (INR)"); plt.legend()
  save("V01_monthly_revenue", f"Revenue peaked in {m.idxmax():%B} and was lowest in {m.idxmin():%B}.")

  # V02
  mp = df.groupby("Month")[PROFIT].sum()
  plt.figure(figsize=(10, 5))
  plt.plot(mp.index, mp.values, marker="o", color="green", label="Profit")
  plt.title("Monthly Profit (2025)")
  plt.xlabel("Month"); plt.ylabel("Profit (INR)"); plt.legend()
  save("V02_monthly_profit", f"Profit was highest in {mp.idxmax():%B}.")

  # V03
  p = df.groupby(PRODUCT)[REV].sum().sort_values()
  plt.figure(figsize=(9, 5))
  plt.barh(p.index, p.values, color="purple")
  plt.title("Net Revenue by Product")
  plt.xlabel("Net Revenue (INR)"); plt.ylabel("Product")
  save("V03_revenue_by_product", f"{p.idxmax()} leads with {p.max()/p.sum()*100:.1f}% of revenue.")

  # V04
  r = df.groupby(REGION)[REV].sum().sort_values(ascending=False)
  plt.figure(figsize=(8, 5))
  plt.bar(r.index, r.values, color="teal")
  plt.title("Net Revenue by Region")
  plt.xlabel("Region"); plt.ylabel("Net Revenue (INR)")
  save("V04_revenue_by_region", f"{r.idxmax()} contributes {r.max()/r.sum()*100:.1f}% of revenue.")

  # V05
  c = df.groupby(CITY)[REV].sum().nlargest(10)
  plt.figure(figsize=(10, 5))
  plt.bar(c.index, c.values, color="orange")
  plt.title("Top 10 Cities by Net Revenue")
  plt.xlabel("City"); plt.ylabel("Net Revenue (INR)")
  plt.xticks(rotation=45, ha="right")
  save("V05_top10_cities", f"{c.index[0]} is the top city; top 10 give {c.sum()/df[REV].sum()*100:.1f}% of revenue.")

  # V06
  ch = df.groupby(CHANNEL)[REV].sum()
  plt.figure(figsize=(7, 7))
  plt.pie(ch.values, labels=ch.index, autopct="%1.1f%%", startangle=90,
          wedgeprops=dict(width=0.4))
  plt.title("Revenue Share by Sales Channel")
  save("V06_channel_donut", f"{ch.idxmax()} is the largest channel at {ch.max()/ch.sum()*100:.1f}%.")

  # V07
  d = df.groupby(DATE)[REV].sum()
  plt.figure(figsize=(12, 5))
  plt.plot(d.index, d.values, alpha=0.4, label="Daily Revenue")
  plt.plot(d.index, d.rolling(7).mean(), color="red", linewidth=2, label="7-Day Moving Avg")
  plt.title("Daily Revenue with 7-Day Moving Average")
  plt.xlabel("Date"); plt.ylabel("Net Revenue (INR)"); plt.legend()
  save("V07_daily_rolling", "The moving average smooths daily noise and shows the underlying trend.")

  # V08
  h = df.pivot_table(index=PRODUCT, columns=REGION, values=REV, aggfunc="sum")
  plt.figure(figsize=(9, 6))
  sns.heatmap(h, annot=True, fmt=".0f", cmap="YlOrBr")
  plt.title("Net Revenue (INR): Product by Region")
  i, j = np.unravel_index(np.nanargmax(h.values), h.shape)
  save("V08_product_region_heatmap", f"Strongest combo: {h.index[i]} in {h.columns[j]}.")

  # V09
  plt.figure(figsize=(8, 5))
  plt.hist(df[DISC], bins=20, color="skyblue", edgecolor="black")
  plt.title("Distribution of Discount Percentage")
  plt.xlabel("Discount (%)"); plt.ylabel("Number of Orders")
  save("V09_discount_hist", f"Most common discount is {df[DISC].mode()[0]}%, mean {df[DISC].mean():.1f}%.")

  # V10
  plt.figure(figsize=(8, 5))
  plt.hist(df[QTY], bins=20, color="salmon", edgecolor="black")
  plt.title("Distribution of Order Quantity")
  plt.xlabel("Quantity (units)"); plt.ylabel("Number of Orders")
  save("V10_quantity_hist", f"Median order size is {df[QTY].median():.0f} units.")

  # V11
  plt.figure(figsize=(8, 6))
  plt.scatter(df[REV], df[PROFIT], alpha=0.5, label="Orders")
  plt.axhline(0, color="red", linestyle="--", label="Break-even")
  plt.title("Net Revenue vs Profit per Order")
  plt.xlabel("Net Revenue (INR)"); plt.ylabel("Profit (INR)"); plt.legend()
  save("V11_revenue_vs_profit",
        f"Correlation {df[REV].corr(df[PROFIT]):.2f}; {(df[PROFIT] < 0).sum()} loss-making orders.")

  # V12
  plt.figure(figsize=(8, 6))
  sns.regplot(data=df, x=DISC, y=QTY, scatter_kws={"alpha": 0.4}, line_kws={"color": "red"})
  plt.title("Discount vs Quantity (with Trend Line)")
  plt.xlabel("Discount (%)"); plt.ylabel("Quantity (units)")
  save("V12_discount_vs_quantity", f"Correlation is {df[DISC].corr(df[QTY]):.2f}.")

  # V13
  plt.figure(figsize=(11, 6))
  sns.boxplot(data=df, x=PRODUCT, y="Margin")
  plt.title("Profit Margin (%) by Product")
  plt.xlabel("Product"); plt.ylabel("Profit Margin (%)")
  plt.xticks(rotation=45, ha="right")
  med = df.groupby(PRODUCT)["Margin"].median()
  save("V13_margin_boxplot", f"Highest median margin: {med.idxmax()} ({med.max():.1f}%); lowest: {med.idxmin()} ({med.min():.1f}%).")

  # V14
  q = df.pivot_table(index="Quarter", columns=REGION, values=REV, aggfunc="sum")
  q.plot(kind="bar", figsize=(10, 6))
  plt.title("Quarterly Net Revenue by Region")
  plt.xlabel("Quarter"); plt.ylabel("Net Revenue (INR)")
  plt.xticks(rotation=0); plt.legend(title="Region")
  save("V14_quarterly_region", f"{q.sum(axis=1).idxmax()} is the strongest quarter.")

  # V15
  plt.figure(figsize=(9, 6))
  sns.countplot(data=df, x=RATING, hue=CHANNEL)
  plt.title("Customer Ratings by Sales Channel")
  plt.xlabel("Customer Rating"); plt.ylabel("Number of Orders")
  plt.legend(title="Sales Channel")
  a = df.groupby(CHANNEL)[RATING].mean()
  save("V15_rating_by_channel", f"Best avg rating: {a.idxmax()} ({a.max():.2f}); lowest: {a.idxmin()} ({a.min():.2f}).")

  # Save all insights to one file
  (Path(report_dir) / "tables" / "chart_insights.txt").write_text("\n".join(insights), encoding="utf-8")