import pandas as pd

# 1. load
df = pd.read_csv("data/employee_payroll.csv")
print(df)


print("First 10 records:")
print(df.head(10))

print("\nLast 10 records:")
print(df.tail(10))


print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nData types:",df.dtypes)
print(df.describe())

print("\nMissing values per column:")
print(df.isnull().sum())


# Remove duplicate employee-month rows
rows_before = len(df)
df = df.drop_duplicates(subset=["EmployeeID", "PayrollMonth"],keep="last").copy()
print("\nDuplicate rows removed:", rows_before - len(df))


# Standardize department and city names

department_map = {
    "it": "IT",
    "i.t.": "IT",
    "information technology": "IT",
    "hr": "HR",
    "h.r.": "HR",
    "human resources": "HR",
    "finance": "Finance",
    "fin": "Finance",
    "sales": "Sales",
    "sales dept": "Sales",
    "operations": "Operations",
    "operation": "Operations",
    "ops": "Operations"
}

df["Department"] = (
    df["Department"]
    .str.strip()
    .str.lower()
    .map(department_map)
)

df["City"] = (
    df["City"]
    .fillna("Unknown")
    .str.strip()
    .str.title()
)

print("\nDepartments after cleaning:", df["Department"].unique())


# Convert joining and payroll dates
df["JoiningDate"] = pd.to_datetime(df["JoiningDate"], format="mixed")
df["PayrollMonth"] = pd.to_datetime(df["PayrollMonth"], format="mixed")


# 12. Gross salary = BasicSalary + HRA + Bonus
df["GrossSalary"] = df["BasicSalary"] + df["HRA"] + df["Bonus"]

# 13. Net Salary
df["NetSalary"] = df["GrossSalary"] - df["Deductions"]


# Attendance percentage
df["AttendancePercentage"] = (df["PresentDays"] / df["WorkingDays"] * 100).round(2)

print("\nRows with salary above 75,000:", len(df[df["GrossSalary"] > 75000]))
print(df[df["GrossSalary"] > 75000].head())