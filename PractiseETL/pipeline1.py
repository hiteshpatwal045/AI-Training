import pandas as pd
from pathlib import Path
from db import engine

BASE_DIR = Path(__file__).resolve().parent
REPORT_DIR = BASE_DIR / "reports"

# Creating Folder


def createfolder() -> None:
    REPORT_DIR.mkdir(exist_ok=True)

# Extracting Data


def extract_data() -> pd.DataFrame:
    employees = pd.read_csv(
        BASE_DIR / "data" / "employees.csv",
        encoding="utf-8-sig"
    )

    employees.columns = (
        employees.columns.astype(str)
        .str.replace("\ufeff", "", regex=False)
        .str.strip()
        .str.lower()
    )
    return employees


# Clean ing Data
def clean_data(emp: pd.DataFrame) -> pd.DataFrame:
    emp = emp.copy()
    emp = emp.drop_duplicates()  # Remove duplicate rows
    emp = emp.dropna(subset=["employee_id"])  # Remove the missing IDs
    emp["employee_id"] = emp["employee_id"].astype(int)

    # String/text
    for col in emp.select_dtypes(include="string"):
        emp[col] = (
            emp[col]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
            .str.title()
        )

    # Numeric columns
    for col in emp.select_dtypes(include=["int64", "float64"]):
        emp[col] = emp[col].fillna(0)

    return emp


# Transform Data
def transform_data(employees: pd.DataFrame) -> pd.DataFrame:
    employees["annual_salary"] = employees["salary"] * 12 * 0.1
    employees["bonus"] = employees["salary"] * 0.1
    employees["salary"] = employees["salary"] * 0.1
    return employees

# Save Cleaned Files


def save_cleaned_data(employees: pd.DataFrame) -> None:
    clean_dir = BASE_DIR / "clean"
    clean_dir.mkdir(exist_ok=True)

    employees.to_csv(
        clean_dir / "cleaned_employees.csv",
        index=False
    )


# Load CSV - MySQL
def load_into_mysql(employees: pd.DataFrame) -> None:
    employees.to_sql(
        name="employees",
        con=engine,
        if_exists="replace",
        index=False
    )

# Main


def main():
    createfolder()
    employees = extract_data()
    employees = clean_data(employees)
    employees = transform_data(employees)
    save_cleaned_data(employees)
    load_into_mysql(employees)
    print("ETL PIPELINE finished")


if __name__ == "__main__":
    main()
