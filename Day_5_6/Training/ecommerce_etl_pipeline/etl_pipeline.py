import re
from datetime import datetime
from pathlib import Path

import pandas as pd
from sqlalchemy import text

from app.database.connection import engine

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_DIR = BASE_DIR / "data" / "input"
REJECTED_DIR = BASE_DIR / "data" / "rejected"

VALID_CUSTOMER_TYPES = ["Regular", "Premium", "Corporate"]
VALID_LOAN_TYPES = [
    "Home Loan",
    "Personal Loan",
    "Car Loan",
    "Education Loan",
    "Business Loan"
]
VALID_LOAN_STATUS = ["Active", "Closed", "Defaulted", "Approved"]

# Create folder


def create_folders() -> None:
    """Create the rejected folder if it does not exist."""
    REJECTED_DIR.mkdir(parents=True, exist_ok=True)

# Extract data


def extract_data() -> tuple[pd.DataFrame,pd.DataFrame]:
    """Read data from CSV files."""
    customers = pd.read_csv(
        INPUT_DIR / "customers.csv",
        encoding="utf-8-sig",
        dtype=str
    ).fillna("")

    loans = pd.read_csv(
        INPUT_DIR / "loans.csv",
        encoding="utf-8-sig",
        dtype=str
    ).fillna("")

    # cleaning all column headings
    for df in [
        customers,
        loans
    ]:
        df.columns = (
            df.columns
            .astype(str)
            .str.replace("\ufeff", "", regex=False)
            .str.strip()
            .str.lower()
        )

    print("Customer columns: ", customers.columns.tolist())
    print("Loans columns: ", loans.columns.tolist())

    return customers, loans

# Validate data


def validate_customers(customers: pd.DataFrame) -> tuple[pd.DataFrame,pd.DataFrame]:
    """Split customers into valid rows and rejected rows."""
    valid_rows = []
    rejected_rows = []
    seen_ids = set()

    for row in customers.to_dict("records"):
        reason = ""

        if row["customer_id"] == "":
            reason = "customer_id is missing"
        elif row["customer_id"] in seen_ids:
            reason = "duplicate customer_id"
        elif row["customer_name"] == "":
            reason = "customer_name is missing"
        elif not re.match(r"^[\w.\-]+@[\w\-]+\.[A-Za-z]{2,}$", row["email"]):
            reason = "invalid email"
        elif not re.fullmatch(r"[6-9][0-9]{9}", row["mobile"]):
            reason = "invalid mobile number"
        elif row["customer_type"] not in VALID_CUSTOMER_TYPES:
            reason = "invalid customer_type"

        seen_ids.add(row["customer_id"])

        if reason == "":
            valid_rows.append(row)
        else:
            row["rejection_reason"] = reason
            rejected_rows.append(row)

    return pd.DataFrame(valid_rows), pd.DataFrame(rejected_rows)


def validate_loans(loans: pd.DataFrame,valid_customer_ids: set) -> tuple[pd.DataFrame,pd.DataFrame]:
    """Split loans into valid rows and rejected rows."""

    valid_rows = []
    rejected_rows = []
    seen_ids = set()

    for row in loans.to_dict("records"):
        reason = ""

        amount = pd.to_numeric(row["loan_amount"], errors="coerce")
        rate = pd.to_numeric(row["interest_rate"], errors="coerce")

        if row["loan_id"] == "":
            reason = "loan_id is missing"
        elif row["loan_id"] in seen_ids:
            reason = "duplicate loan_id"
        elif row["customer_id"] == "":
            reason = "customer_id is missing"
        elif row["customer_id"] not in valid_customer_ids:
            reason = "customer does not exist"
        elif pd.isna(amount) or amount <= 0:
            reason = "loan_amount must be greater than zero"
        elif pd.isna(rate) or rate <= 0:
            reason = "interest_rate must be greater than zero"
        elif row["loan_type"] not in VALID_LOAN_TYPES:
            reason = "invalid loan_type"
        elif row["loan_status"] not in VALID_LOAN_STATUS:
            reason = "invalid loan_status"

        seen_ids.add(row["loan_id"])

        if reason == "":
            valid_rows.append(row)
        else:
            row["rejection_reason"] = reason
            rejected_rows.append(row)

    return pd.DataFrame(valid_rows), pd.DataFrame(rejected_rows)

# Save rejected records


def save_rejected_records(rejected_customers: pd.DataFrame,rejected_loans: pd.DataFrame,run_id: str) -> None:
    """Save rejected records as CSV files."""
    rejected_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    rejected_customers["rejected_at"] = rejected_at
    rejected_customers["pipeline_run_id"] = run_id

    rejected_loans["rejected_at"] = rejected_at
    rejected_loans["pipeline_run_id"] = run_id

    rejected_customers.to_csv(
        REJECTED_DIR / "rejected_customers.csv",
        index=False
    )
    rejected_loans.to_csv(
        REJECTED_DIR / "rejected_loans.csv",
        index=False
    )

# Transform data


def transform_data(customers: pd.DataFrame,loans: pd.DataFrame) -> tuple[pd.DataFrame,pd.DataFrame]:
    """Convert text columns into proper dates and numbers."""
    customers = customers.copy()
    loans = loans.copy()

    customers["registration_date"] = pd.to_datetime(
        customers["registration_date"]
    ).dt.date

    loans["loan_amount"] = loans["loan_amount"].astype(float)

    loans["interest_rate"] = loans["interest_rate"].astype(float)

    loans["loan_start_date"] = pd.to_datetime(
        loans["loan_start_date"]
    ).dt.date

    return customers, loans

# Load data into MySQL


def load_data(customers: pd.DataFrame,loans: pd.DataFrame) -> None:
    """Clear old data and load valid records into MySQL."""
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM loans"))
        conn.execute(text("DELETE FROM customers"))

    customers.to_sql(
        "customers",
        engine,
        if_exists="append",
        index=False
    )
    loans.to_sql(
        "loans",
        engine,
        if_exists="append",
        index=False
    )


def run_pipeline() -> None:
    """Execute the complete pipeline"""

    print("Starting Banking Data Pipeline....")

    run_id = datetime.now().strftime("RUN_%Y%m%d_%H%M%S")

    create_folders()

    print("Step 1. Extracting Data....")
    customers, loans = extract_data()

    print("Step 2. Validating Customers....")
    valid_customers, rejected_customers = validate_customers(customers)

    print("Step 3. Validating Loans....")
    valid_customer_ids = set(valid_customers["customer_id"])
    valid_loans, rejected_loans = validate_loans(loans, valid_customer_ids)

    print("Step 4. Saving Rejected Records....")
    save_rejected_records(rejected_customers, rejected_loans, run_id)

    print("Step 5. Transforming Data....")
    valid_customers, valid_loans = transform_data(valid_customers, valid_loans)

    print("Step 6. Loading Data into MySQL....")
    load_data(valid_customers, valid_loans)

    print("\nPipeline Summary")
    print("==========================")
    print("Customers received :", len(customers))
    print("Customers loaded   :", len(valid_customers))
    print("Customers rejected :", len(rejected_customers))
    print("Loans received     :", len(loans))
    print("Loans loaded       :", len(valid_loans))
    print("Loans rejected     :", len(rejected_loans))

    print("\nPipeline completed successfully")
    print(f"Rejected folder : {REJECTED_DIR}")


if __name__ == "__main__":
    run_pipeline()