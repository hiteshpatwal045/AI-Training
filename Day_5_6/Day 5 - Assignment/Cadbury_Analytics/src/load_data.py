import pandas as pd

def load_all_data(data_dir):
  """Read the 3 CSV files and return them."""
  sales = pd.read_csv(data_dir / "Cadbury_Dairy_Milk_Sales_2025_Synthetic.csv")
  products = pd.read_csv(data_dir / "Cadbury_Product_Master.csv")
  stores = pd.read_csv(data_dir / "Cadbury_Store_Master.csv")
  print("Sales:", sales.shape)
  print("Products:", products.shape)
  print("Stores:", stores.shape)

  # P02. Display the first 10 records.
  print("P02\n", sales.head(10))

  # P03. Display the last 10 records.
  print("P03\n", sales.tail(10))

  # P04. Find the number of rows and columns.
  print("P04 rows, columns:", sales.shape)

  # P05. List all column names.
  print("P05", list(sales.columns))

  # P06. Inspect column data types.
  print("P06\n", sales.dtypes)

  # P07. Generate a concise DataFrame information summary.
  print("P07")
  sales.info()

  # P08. Calculate descriptive statistics for numeric fields.
  print("P08\n", sales.describe())

  # P09. Calculate descriptive statistics for categorical fields.
  print("P09\n", sales.describe(include="object"))

  # P10. Identify missing values by column.
  print("P10\n", sales.isna().sum())

  # P11. Count duplicate Order_ID values.
  print("P11", sales["Order_ID"].duplicated().sum())

  # P12. Find unique product names and their count.
  print("P12", sales["Product_Name"].unique())
  print("P12 count:", sales["Product_Name"].nunique())

  # P13. Find unique cities and regions.
  print("P13 cities:", sales["City"].unique())
  print("P13 regions:", sales["Region"].unique())

  # P14. Convert Order_Date to datetime and verify the result.
  sales["Order_Date"] = pd.to_datetime(sales["Order_Date"])
  print("P14", sales["Order_Date"].dtype)

  return sales, products, stores