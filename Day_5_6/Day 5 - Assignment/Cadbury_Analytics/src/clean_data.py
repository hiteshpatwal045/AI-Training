import numpy as np
import pandas as pd


def clean_sales_data(sales):
  """Clean the sales data and add new columns (P16-P30)."""

  # P16: work on a copy so the raw data stays safe
  df = sales.copy()

  # P17: remove exact duplicate rows
  before = len(df)
  df = df.drop_duplicates()
  print("P17 duplicate rows removed:", before - len(df))

  # P18: consistent column names (no spaces at the ends, underscores instead of spaces)
  df.columns = df.columns.str.strip().str.replace(" ", "_")

  # P19: Quantity must be positive
  print("P19 rows with Quantity <= 0:", (df["Quantity"] <= 0).sum())

  # P20: Discount_Pct must be between 0 and 100
  bad_discount = (df["Discount_Pct"] < 0) | (df["Discount_Pct"] > 100)
  print("P20 rows with discount outside 0-100:", bad_discount.sum())

  # P21: negative revenue, cost or profit
  print("P21 negative revenue rows:", (df["Net_Revenue_INR"] < 0).sum())
  print("P21 negative cost rows:", (df["Total_Cost_INR"] < 0).sum())
  print("P21 negative profit rows (loss-making orders):", (df["Profit_INR"] < 0).sum())
  # Meaning: negative profit = the order lost money because product cost
  # plus delivery cost was more than the revenue.

  # P22: recalculate revenue
  df["Net_Revenue_Recalc"] = df["Quantity"] * df["Unit_Selling_Price_INR"]

  # P23: compare recorded and recalculated revenue (tolerance of 0.01 rupee)
  revenue_diff = (df["Net_Revenue_INR"] - df["Net_Revenue_Recalc"]).abs()
  print("P23 revenue mismatches:", (revenue_diff > 0.01).sum())

  # P24: recalculate profit
  df["Profit_Recalc"] = (
    df["Net_Revenue_INR"] - df["Total_Cost_INR"] - df["Delivery_Cost_INR"]
  )
  profit_diff = (df["Profit_INR"] - df["Profit_Recalc"]).abs()
  print("P24 profit mismatches:", (profit_diff > 0.01).sum())

  # P25: profit margin %, safe division (if revenue is 0, margin is 0)
  df["Profit_Margin_Pct"] = np.where(
    df["Net_Revenue_INR"] != 0,
    df["Profit_INR"] / df["Net_Revenue_INR"] * 100,
    0,
  )

  # P14 (again): make sure the date column is a real date
  df["Order_Date"] = pd.to_datetime(df["Order_Date"])

  # P26: Year, Month, Month_Name
  df["Year"] = df["Order_Date"].dt.year
  df["Month"] = df["Order_Date"].dt.month
  df["Month_Name"] = df["Order_Date"].dt.month_name()

  # P27: Quarter and Weekday
  df["Quarter"] = df["Order_Date"].dt.quarter
  df["Weekday"] = df["Order_Date"].dt.day_name()

  # P28: Weekend_Flag (Saturday = 5, Sunday = 6)

  # P29: Discount_Band

  # P30: Order_Value_Band using quantiles (4 equal groups)

  return df