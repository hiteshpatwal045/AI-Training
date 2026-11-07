from pathlib import Path
import pandas as pd

# create_folders()

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"
DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "ecommerce_warehouse.db"


def create_folders() -> None:
    """Create report and database folders if they do not exist"""
    DATA_DIR.mkdir(exist_ok=True)
    REPORT_DIR.mkdir(exist_ok=True)
    DATABASE_DIR.mkdir(exist_ok=True)


def extract_data() -> tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame
]:
    """Read data from CSV files."""
    customers = pd.read_csv(
        DATA_DIR / "customers.csv",
        encoding="utf-8-sig"
    )

    orders = pd.read_csv(
        DATA_DIR / "orders.csv",
        encoding="utf-8-sig"
    )

    payments = pd.read_csv(
        DATA_DIR / "payments.csv",
        encoding="utf-8-sig"
    )

    deliveries = pd.read_csv(
        DATA_DIR / "deliveries.csv",
        encoding="utf-8-sig"
    )

    # cleaning all column headings
    for df in [
        customers,
        orders,
        payments,
        deliveries
    ]:
        df.columns = (
            df.columns
            .astype(str)
            .str.replace("\ufeff", "", regex=False)
            .str.strip()
            .str.lower()
        )

    print("Customer columns: ", customers.columns.tolist())
    print("Orders columns: ", orders.columns.tolist())
    print("payments columns: ", payments.columns.tolist())
    print("deliveries columns: ", deliveries.columns.tolist())

    return customers, orders, payments, deliveries

# extract_data()


def clean_customers(customers: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate customers and clean customer fields/"""
    customers = customers.copy()

    customers = customers.drop_duplicates(
        subset=["customer_id"]
    )

    customers["customer_name"] = (
        customers["customer_name"]
        .fillna("Unknown Customer")
        .astype(str)
        .str.strip()
        .str.title()
    )

    customers["email"] = (
        customers["email"]
        .fillna("Unkown@email.com")
        .astype(str)
        .str.strip()
        .str.lower()
    )

    customers["city"] = (
        customers["city"]
        .fillna("unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    return customers


def clean_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate columns"""
    orders = orders.copy()

    orders = orders.drop_duplicates(
        subset=["order_id"]
    )

    orders["customer_id"] = (
        orders["customer_id"]
        .fillna("Unknown Customer")
        .astype(str)
        .str.strip()
        .str.title()
    )

    orders["product_name"] = (
        orders["product_name"]
        .fillna("Unknow Product")
        .astype(str)
        .str.strip()
        .str.title()
    )

    orders["quantity"] = pd.to_numeric(
        orders["quantity"],
        errors="coerce"
    ).fillna(0)

    orders["unit_price"] = pd.to_numeric(
        orders["unit_price"],
        errors="ecoerce"
    ).fillna(0)

    orders["order_date"] = pd.to_datetime(
        orders["order_date"],
        errors="coerce"
    )

    orders["total_amount"] = (
        orders["quantity"] * orders["unit_price"]
    )
    return orders


def clean_payments(payments: pd.DataFrame) -> pd.DataFrame:
    """Remove Duplicates Columns"""
    payments = payments.copy()

    payments = payments.drop_duplicates(
        subset=["payment_id"]
    )

    payments["payment_status"] = (
        payments["payments_status"]
        .fillna("Unknow")
        .astype(str)
        .str.strip()
        .str.title()
    )

    payments["payment_method"] = (
        payments["payment_method"]
        .fillna("unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    payments["payment_date"] = pd.to_datetime(
        payments["payment_date"],
        errors="coerce"
    )

    return payments


def clean_deliveries(deliveries: pd.DataFrame) -> pd.DataFrame:
    """remove duplicate """
    deliveries = deliveries.copy()

    deliveries = deliveries.drop_duplicates(
        subset=["delivery_id"]
    )

    deliveries["delivery_status"] = (
        deliveries["delivery_status"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    deliveries["delivery_city"] = (
        deliveries["delivery_city"]
        .fillna("unknow")
        .astype(str)
        .str.strip()
        .str.title()
    )
    return deliveries


# Joins all Dataset

def join_data(
    customers: pd.DataFrame,
    orders: pd.DataFrame,
    payments: pd.DataFrame,
    deliveries: pd.DataFrame
) -> pd.DataFrame:
    """Join customers, orderes, payments, and deliveries"""
    combined_data = orders.merge(
        customers,
        on="customer_id",
        how="left"
    )
    combined_data = combined_data.merge(
        payments,
        on="order_id",
        how="left"
    )
    combined_data = combined_data.merge(
        deliveries,
        on="order_id",
        how="left"
    )

    combined_data["customer_name"] = (
        combined_data["customer_name"]
        .fillna("Unknown Customer")
    )

    combined_data["city"] = (
        combined_data["city"]
        .fillna("Unknown City")
    )

    combined_data["payment_status"] = (
        combined_data["payment_status"]
        .fillna("Unknown Payments")
    )

    combined_data["delivery_status"] = (
        combined_data["delivery_status"]
        .fillna("Unknown Delievery Status")
    )

    return combined_data

# generate total orders report


def generate_total_orders_report(combined_data: pd.DataFrame) -> pd.DataFrame:
    """calculate total number of unique orders."""
    total_orders = combined_data["order_id"].nunique()
    return pd.DataFrame(
        {
            "metric": ["total Order"],
            "value": [total_orders]
        }
    )


# Generate Total revenue report

def generate_total_revenue_report(combined_data: pd.DataFrame) -> pd.DataFrame:
    """Calculate revenue from successful payments."""
    successfull_orders = combined_data[
        combined_data["payment_status"] == "Success"
    ]

    total_revenue = successfull_orders["total_amount"].sum()

    return pd.DataFrame(
        {
            "metric": ["Total Revenue"],
            "value": [total_revenue]
        }
    )
