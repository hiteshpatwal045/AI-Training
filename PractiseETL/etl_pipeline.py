from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Paths
BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"
CSV_PATH = DATA_DIR / "employees.csv"

# Create Folder

def create_folders() -> None:
    REPORT_DIR.mkdir(exist_ok=True)

# Extract Data

def extract_data() -> pd.DataFrame:
    employees = pd.read_csv(
        CSV_PATH,
        encoding="utf-8-sig"
    )
    employees.columns = (
        employees.columns
        .astype(str)
        .str.replace("\ufeff", "", regex=False)
        .str.strip()
        .str.lower()
    )
    print("Columns:", employees.columns.tolist())
    return employees

# Clean Data
def clean_employees(employees: pd.DataFrame) -> pd.DataFrame:

    employees = employees.copy()
    employees = employees.drop_duplicates(subset=["employee_id"])
    employees["employee_name"] = (
        employees["employee_name"]
        .fillna("Unknown Employee")
        .astype(str)
        .str.strip()
        .str.title()
    )

    employees["department"] = (
        employees["department"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    employees["salary"] = pd.to_numeric(
        employees["salary"],
        errors="coerce"
    ).fillna(0)

    employees["email"] = (
        employees["email"]
        .fillna("unknown@gmail.com")
        .astype(str)
        .str.strip()
        .str.lower()
    )

    return employees

# Reports
def generate_employee_count_report(employees: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
            "metric": ["Total Employees"],
            "value": [employees["employee_id"].nunique()]
        }
    )

def generate_department_report(employees: pd.DataFrame) -> pd.DataFrame:
    return (
        employees.groupby(
            "department",
            as_index=False
        )
        .agg(
            employee_count=("employee_id", "count"),
            total_salary=("salary", "sum")
        )
    )

def generate_top_salary_report(employees: pd.DataFrame) -> pd.DataFrame:
    return (
        employees.sort_values(
            by="salary",
            ascending=False
        )
        .head(10)
    )

# Save Reports
def save_reports(
    employee_count_report: pd.DataFrame,
    department_report: pd.DataFrame,
    top_salary_report: pd.DataFrame
) -> None:
    employee_count_report.to_csv(REPORT_DIR / "employee_count.csv",index=False)
    department_report.to_csv(REPORT_DIR / "department_report.csv",index=False)
    top_salary_report.to_csv(REPORT_DIR / "top_salary_report.csv",index=False)

# Chart
def create_department_chart(employees: pd.DataFrame):

    dept_data = (
        employees["department"]
        .value_counts()
    )

    plt.figure(figsize=(8, 5))

    plt.bar(
        dept_data.index,
        dept_data.values,
        color="skyblue"
    )

    plt.title("Employees by Department")
    plt.xlabel("Department")
    plt.ylabel("Employee Count")

    plt.tight_layout()

    plt.savefig(REPORT_DIR / "department_chart.png")
    plt.close()

# ETL Pipeline
def run_etl_pipeline() -> None:
    print("Starting Employee ETL Pipeline")
    create_folders()

    employees = extract_data()
    employees = clean_employees(employees)

    employee_count_report = (generate_employee_count_report(employees))
    department_report = (generate_department_report(employees))
    top_salary_report = (generate_top_salary_report(employees))
    save_reports(employee_count_report,department_report,top_salary_report)
    create_department_chart(employees)

    print(employee_count_report)
    print(department_report)
    print(top_salary_report)

if __name__ == "__main__":
    run_etl_pipeline()