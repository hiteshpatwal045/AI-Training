from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# create_folders()

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"
DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "ecommerce_warehouse.db"

# Create folder


def create_folders() -> None:
    """Create report and database folders if they do not exist"""
    DATA_DIR.mkdir(exist_ok=True)
    REPORT_DIR.mkdir(exist_ok=True)
    DATABASE_DIR.mkdir(exist_ok=True)

# Extract data and load data


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
            # convert every col into str
            .astype(str)
            # replace ByteOrderMark from every col and replce it with "",
            .str.replace("\ufeff", "", regex=False)
            .str.strip()
            .str.lower()
        )

    print("Customer columns: ", customers.columns.tolist())
    print("Orders columns: ", orders.columns.tolist())
    print("payments columns: ", payments.columns.tolist())
    print("deliveries columns: ", deliveries.columns.tolist())

    return customers, orders, payments, deliveries

# clean data


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
        errors="coerce"
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
        payments["payment_status"]
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

# Generate top products reports


def generate_top_products_report(combined_data: pd.DataFrame) -> pd.DataFrame:
    """Find the top 10 selling products."""

    successfull_order = combined_data[
        combined_data["payment_status"] == "Success"
    ]

    top_products = (
        successfull_order
        .groupby("product_name", as_index=False)
        .agg(
            total_quantity_sold=("quantity", "sum"),
            total_product_revenue=("total_amount", "sum")
        )
        .sort_values(
            by="total_quantity_sold",
            ascending=False
        )
        .head(10)
    )
    return top_products

# Generate Top Customers Report


def generate_top_customers_report(combined_data: pd.DataFrame) -> pd.DataFrame:
    """Find the tope 10 customers by total spending"""

    successfull_orders = combined_data[
        combined_data["payment_status"] == "Success"
    ]

    top_customers = (
        successfull_orders
        .groupby(
            ["customer_id", "customer_name"],
            as_index=False
        )
        .agg(
            total_orders=("order_id", "nunique"),
            total_spent=("total_amount", "sum")
        )
        .sort_values(
            by="total_spent",
            ascending=False
        )
        .head(10)
    )

    return top_customers

# Generate Failed Payments Reports


def generate_failed_payments_report(combined_data: pd.DataFrame) -> pd.DataFrame:
    """Create a report contianing failed payments."""

    failed_payments = combined_data[
        combined_data["payment_status"] == "Failed"
    ]

    required_columns = [
        "payment_id",
        "order_id",
        "customer_id",
        "customer_name",
        "product_name",
        "total_amount",
        "payment_method",
        "payment_status"
    ]

    return failed_payments[required_columns]


# save reports to CSV files
def save_reports(
    total_orders_reports: pd.DataFrame,
    total_revenue_report: pd.DataFrame,
    top_products_report: pd.DataFrame,
    top_customers_report: pd.DataFrame,
    failed_payments_report: pd.DataFrame
) -> None:
    """Save all generated reports as CSV Files."""

    total_orders_reports.to_csv(
        REPORT_DIR / "total_orders.csv",
        index=False
    )
    total_revenue_report.to_csv(
        REPORT_DIR / "total_revenue.csv",
        index=False
    )
    top_products_report.to_csv(
        REPORT_DIR / "total_10_products.csv",
        index=False
    )
    top_customers_report.to_csv(
        REPORT_DIR / "total_customers.csv",
        index=False
    )
    failed_payments_report.to_csv(
        REPORT_DIR / "failed_payments.csv",
        index=False
    )


# data visualization
def create_sales_line_chart(combined_data):
    sales = combined_data[
        combined_data["payment_status"] == "Success"
    ].copy()

    sales = sales.dropna(subset=["order_date"])

    daily_sales = (
        sales.groupby("order_date")["total_amount"]
        .sum()
        .sort_index()
    )

    plt.figure(figsize=(10, 5)),

    plt.plot(
        daily_sales.index,
        daily_sales.values,
        marker='o',
        color="blue"
    )
    plt.title("Daily Sales Revenue")
    plt.xlabel("Order Date")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.grid(True)

    plt.tight_layout()

    plt.savefig(REPORT_DIR / "sales_line_chart.png")
    plt.close()

# Pie Chart - Payment Status


def create_payment_pie_charts(combined_data):

    payment_counts = (
        combined_data
        .drop_duplicates(subset=["payment_id"])
        ["payment_status"]
        .value_counts()
    )

    type(payment_counts)
    print("Payment Status Counts:\n", payment_counts)

    plt.figure(figsize=(7, 7))

    plt.pie(
        payment_counts.values,
        labels=payment_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Payment status Distribution")

    plt.tight_layout()

    plt.savefig(REPORT_DIR / "payment_pie_chart.png")
    plt.close()


def run_etl_pipeline() -> None:
    """Execute the complete ETL pipeline"""

    print("Starting E-Commerce ETL Pipeline....")

    create_folders()

    print("Step 1. Extracting Data....")
    customers, orders, payments, deliveries = extract_data()

    print("Cleaning data.....")

    print("2. Customer Data....")
    customers = clean_customers(customers)
    print("3. Order Data....")
    orders = clean_orders(orders)
    print("4. Payments Data...")
    payments = clean_payments(payments)
    print("5. Deliveries Data...")
    deliveries = clean_deliveries(deliveries)

    print("Step 6. Joining Datasets")
    combined_data = join_data(customers, orders, payments, deliveries)
    print(combined_data)

    print("step 7. Generating reports")
    print("==========================")

    total_orders_reports = generate_total_orders_report(
        combined_data
    )
    print("\nTotal Orders Report")
    print(total_orders_reports)

    total_revenue_reports = generate_total_revenue_report(
        combined_data
    )
    print("\nRevenue Report")
    print(total_revenue_reports)

    top_products_report = generate_top_products_report(combined_data)
    print("\nTop products report")
    print(top_products_report)

    top_customers_report = generate_top_customers_report(combined_data)
    print("\nTop Customers")
    print(top_customers_report)

    failed_payments_report = generate_failed_payments_report(combined_data)
    print("\nFailed Payments")
    print(failed_payments_report)

    print("Step 8. Save Report")
    print("===============================")
    save_reports(total_orders_reports,
                 total_revenue_reports,
                 top_products_report,
                 top_customers_report,
                 failed_payments_report
                 )

    print("Step 9. Data Visualization")
    print("==========================")
    create_sales_line_chart(combined_data)
    create_payment_pie_charts(combined_data)

    print("\nETL pipeline completed successfully")
    print(f"Report folder : {REPORT_DIR}")
    print(f"Database folder: {DATABASE_DIR}")


if __name__ == "__main__":
    run_etl_pipeline()
