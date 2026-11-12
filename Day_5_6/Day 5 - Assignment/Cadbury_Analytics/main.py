from pathlib import Path

from src.load_data import load_all_data
from src.clean_data import clean_sales_data
from src.panda_analysis import run_pandas_analysis
from src.numpy_analysis import run_numpy_analysis

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"


def main():
  (REPORT_DIR / "charts").mkdir(parents=True, exist_ok=True)
  (REPORT_DIR / "tables").mkdir(parents=True, exist_ok=True)

  sales, products, stores = load_all_data(DATA_DIR)
  print("Step 1 finished.")

  clean_sales = clean_sales_data(sales)
  print(clean_sales.shape)
  print("Step 2 finished.")

  merged = run_pandas_analysis(clean_sales, products, stores, REPORT_DIR)
  print(merged.shape)
  print("step 3 finished")

  run_numpy_analysis(merged)
  print("Step 4 finished.")


if __name__ == "__main__":
  main()