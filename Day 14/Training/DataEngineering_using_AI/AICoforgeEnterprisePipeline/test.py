import pandas as pd
import numpy as np

df1 = pd.read_csv("data/employees/finance_employees.csv")
df2 = pd.read_csv("data/employees/hr_employees.csv")
df3 = pd.read_csv("data/employees/it_employees.csv")
df4 = pd.read_csv("data/employees/operations_employees.csv")
df5 = pd.read_csv("data/employees/sales_employees.csv")


print("==========================================================")
print(df1.head(3))
print("==========================================================")
print(df2.head(3))
print("==========================================================")
print(df3.head(3))
print("==========================================================")
print(df4.head(3))
print("==========================================================")
print(df5.head(3))
print("==========================================================")


print("==========================================================")
print("======concat====")
employee_df = pd.concat([df1, df2, df3, df4, df5])
print(employee_df.tail(5))

print("==========================================================")
print("====== First 20 records ====")
print(employee_df.head(20))

print("====== Last 20 records ====")
print(employee_df.tail(20))

print("====== total no of emp across all department =====")
result = employee_df.groupby("department")["emp_name"].count()
print(result)


print("====== columns and dtype =====")
result1 = employee_df.columns
result2 = employee_df.dtypes
print(result1)
print(result2)


print("====== count of is null  ====")
result1 = employee_df.isna().sum()
print(result1)

print("====== Missing values =====")
result = employee_df.duplicated()
print(result)

print("====== Identify duplicate records based on emp_id.=====")
result = employee_df.duplicated(subset="emp_id")
print(result)


print("====== Display the number of employees in each department. =====")
result = employee_df.groupby("department")["emp_id"].count()
print(result)

print("====== Find the total number of unique cities in the dataset. =====")
result = employee_df["city"].unique()
print(result)


print("====== Display all employees working in the IT department.  ======")
# result = employee_df[employee_df["department"] == "IT"]
result = employee_df.query("department == 'IT'")
print(result)


print("====== Find employees working in the Finance department =====")
# result = employee_df[employee_df["department"] == "Finance"]
result = employee_df.query("department == 'Finance'")
print(result)


print("======  Display employees whose salary is greater than ₹100,000. =====")
result = employee_df[employee_df[""] > 100000]

print("======  ====")

print("======  ====")

print("======  ====")

print("======  ====")

print("======  ====")

print("======  ====")

print("======  ====")


print("======  ====")
