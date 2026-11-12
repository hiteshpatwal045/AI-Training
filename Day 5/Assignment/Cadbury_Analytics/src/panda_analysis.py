import pandas as pd

def selection_filtering_sorting(df):
  """P31-P45: select, filter and sort."""

  # P31. Select Order_ID, Product_Name, City, Quantity and Net_Revenue_INR.
  print(df[["Order_ID", "Product_Name", "City", "Quantity", "Net_Revenue_INR"]].head())

  # P32. Filter transactions from Mumbai.
  print(df[df["City"] == "Mumbai"].head())

  # P33. Filter orders for Dairy Milk Silk.
  print(df[df["Product_Name"] == "Dairy Milk Silk"].head())

  # P34. Filter transactions with Quantity >= 10.
  print(df[df["Quantity"] >= 10].head())

  # P35. Filter orders with Discount_Pct >= 15.
  print(df[df["Discount_Pct"] >= 15].head())

  # P36. Find loss-making orders where Profit_INR < 0.
  print(df[df["Profit_INR"] < 0].head())

  # P37. Find orders from North region placed in Q4.
  print(df[(df["Region"] == "North") & (df["Quarter"] == 4)].head())

  # P38. Filter e-commerce orders paid by UPI.
  print(df[(df["Sales_Channel"] == "E-commerce") & (df["Payment_Method"] == "UPI")].head())

  # P39. Find orders between two user-selected dates.
  print(df[(df["Order_Date"] >= "2025-03-01") & (df["Order_Date"] <= "2025-03-31")].head())

  # P40. Find orders where Product_Name contains Dairy Milk.
  print(df[df["Product_Name"].str.contains("Dairy Milk")].head())

  # P41. Find transactions with Customer_Rating <= 2.
  print(df[df["Customer_Rating"] <= 2].head())

  # P42. Sort orders by Net_Revenue_INR descending.
  print(df.sort_values("Net_Revenue_INR", ascending=False).head())

  # P43. Show the top 20 orders by Profit_INR.
  print(df.nlargest(20, "Profit_INR"))

  # P44. Sort by Region ascending then Quantity descending.
  print(df.sort_values(["Region", "Quantity"], ascending=[True, False]).head())

  # P45. Select transactions meeting three simultaneous business conditions.
  print(df[(df["Sales_Channel"] == "E-commerce") & (df["Discount_Pct"] >= 15) & (df["Profit_INR"] < 0)])


def aggregation_metrics(df):
  """P46-P60: totals and business metrics."""

  # P46. Calculate total net revenue.
  total_revenue = df["Net_Revenue_INR"].sum()
  print(total_revenue)

  # P47. Calculate total profit.
  total_profit = df["Profit_INR"].sum()
  print(total_profit)

  # P48. Calculate total quantity sold.
  print(df["Quantity"].sum())

  # P49. Calculate overall profit margin percentage.
  print(total_profit / total_revenue * 100)

  # P50. Calculate average order value.
  print(df["Net_Revenue_INR"].mean())

  # P51. Count orders by Sales_Channel.
  print(df["Sales_Channel"].value_counts())

  # P52. Calculate revenue by Product_Name.
  print(df.groupby("Product_Name")["Net_Revenue_INR"].sum())

  # P53. Calculate profit by Region.
  print(df.groupby("Region")["Profit_INR"].sum())

  # P54. Calculate units sold by City.
  print(df.groupby("City")["Quantity"].sum())

  # P55. Find the top five products by revenue.
  print(df.groupby("Product_Name")["Net_Revenue_INR"].sum().nlargest(5))

  # P56. Find the bottom five cities by profit.
  print(df.groupby("City")["Profit_INR"].sum().nsmallest(5))

  # P57. Calculate mean and median discount by channel.
  print(df.groupby("Sales_Channel")["Discount_Pct"].agg(["mean", "median"]))

  # P58. Calculate revenue and profit grouped by Region and Product_Name.
  print(df.groupby(["Region", "Product_Name"])[["Net_Revenue_INR", "Profit_INR"]].sum())

  # P59. Calculate order count, revenue, and average rating by Customer_Segment.
  print(df.groupby("Customer_Segment").agg(
    Orders=("Order_ID", "count"),
    Revenue=("Net_Revenue_INR", "sum"),
    Avg_Rating=("Customer_Rating", "mean")))

  # P60. Calculate return rate by product using Returned_Flag.
  print(df.groupby("Product_Name")["Returned_Flag"].mean() * 100)


def advanced_analytics(df, products, stores, report_dir):
  # """P61-P75: trends, pivots, rankings and joins. Returns the merged data."""

  # # P61. Build a monthly revenue trend table.
  monthly = df.groupby("Month")["Net_Revenue_INR"].sum()
  print(monthly)

  # # P62. Compute month-over-month revenue growth percentage.

  # # P63. Build a quarterly profit comparison.
  print(df.groupby("Quarter")["Profit_INR"].sum())

  # # P64. Create a pivot table: Region by Product_Name with revenue totals.

  # # P65. Create a pivot table: Sales_Channel by Month with order counts.

  # # P66. Create a cross-tab of Customer_Segment versus Payment_Method.

  # # P67. Calculate a seven-day rolling revenue average on daily totals.

  # # P68. Calculate cumulative revenue over time.

  # # P69. Rank products within each region by revenue.

  # # P70. Calculate each product share of total revenue.

  # # P71. Merge sales with the product master on Product_ID.
  merged = df.merge(products[["Product_ID", "Standard_MRP_INR"]], on="Product_ID")
  print(merged.shape)

  # # P72. Merge sales with the store master on Store_ID.


  # # P73. Compare actual unit MRP with standard product master MRP.

  # # P74. Calculate store-level revenue, profit, order count and average order value.

  # # P75. Identify top-performing stores and prepare a five-point management summary.
  return merged

def run_pandas_analysis(clean_sales, products, stores, report_dir):
  """Runs all pandas sections (P31-P75) and returns the merged data."""
  (report_dir / "tables").mkdir(parents=True, exist_ok=True)

  selection_filtering_sorting(clean_sales)
  aggregation_metrics(clean_sales)
  merged = advanced_analytics(clean_sales, products, stores, report_dir)

  return merged