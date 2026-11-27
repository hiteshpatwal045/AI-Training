import pandas as pd
from pathlib import Path
from db import engine

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
CLEAN_DIR = BASE_DIR / "clean"
REPORT_DIR = BASE_DIR / "reports"


# 1. Create Folders
def create_folders() -> None:
    REPORT_DIR.mkdir(exist_ok=True)
    CLEAN_DIR.mkdir(exist_ok=True)


# 2. Extract Data
def extract_data(filename: str) -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / filename, encoding="utf-8-sig")
    df.columns = (
        df.columns.astype(str)
        .str.replace("\ufeff", "", regex=False)
        .str.strip()
        .str.lower()
    )
    return df


# 3. Clean Data
def clean_data(df: pd.DataFrame, id_col: str) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates()
    df = df.dropna(subset=[id_col])
    df[id_col] = df[id_col].astype(int)

    for col in df.select_dtypes(include=["object", "string"]):
        df[col] = df[col].fillna("Unknown").astype(str).str.strip()

        if col == "email":
            df[col] = df[col].str.lower()
        elif col == "department_name":
            # Keeps "IT" and "HR" uppercase while title-casing others
            df[col] = df[col].apply(
                lambda x: x.upper() if len(x) <= 2 else x.title())
        else:
            df[col] = df[col].str.title()

    for col in df.select_dtypes(include=["int64", "float64"]):
        df[col] = df[col].fillna(0)

    return df


# 4. Transform Employees Data
def transform_employees(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.copy()
    employees["annual_salary"] = employees["salary"] * 12
    employees["bonus"] = employees["salary"] * 0.10
    return employees


# 5. Merge Employees & Departments
def merge_data(employees: pd.DataFrame, departments: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(employees, departments, on="department_id", how="left")


# 6. Save Cleaned CSVs
def save_cleaned_data(df: pd.DataFrame, output_filename: str) -> None:
    df.to_csv(CLEAN_DIR / output_filename, index=False)


# 7. Load into MySQL
def load_into_mysql(df: pd.DataFrame, table_name: str) -> None:
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )


# 8. Run ETL for Both Files
def run_etl() -> None:
    create_folders()

    # --- File 1: Employees ---
    employees = extract_data("employees.csv")
    employees = clean_data(employees, id_col="employee_id")
    employees = transform_employees(employees)
    save_cleaned_data(employees, "cleaned_employees.csv")
    load_into_mysql(employees, "employees")

    # --- File 2: Departments ---
    departments = extract_data("departments.csv")
    departments = clean_data(departments, id_col="department_id")
    save_cleaned_data(departments, "cleaned_departments.csv")
    load_into_mysql(departments, "departments")

    # --- Combined Table ---
    employee_details = merge_data(employees, departments)
    save_cleaned_data(employee_details, "cleaned_employee_details.csv")
    load_into_mysql(employee_details, "employee_details")

    print("ETL PIPELINE finished for both files!")


if __name__ == "__main__":
    run_etl()
