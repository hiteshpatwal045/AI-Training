import pandas as pd

# Dataset 1: Managers (20 Records)
managers_data = {
    "manager_id": [
        "M001", "M002", "M003", "M004", "M005", "M006", "M007", "M008", "M009", "M010",
        "M011", "M012", "M013", "M014", "M015", "M016", "M017", "M018", "M019", "M020"
    ],
    "manager_name": [
        "Amit Sharma", "Priya Nair", "Rahul Mehta", "Neha Kapoor", "Vikram Singh",
        "Anjali Rao", "Karan Shah", "Sneha Iyer", "Rohit Verma", "Pooja Gupta",
        "Arjun Patel", "Meera Joshi", "Nikhil Das", "Ritu Malhotra", "Sanjay Kulkarni",
        "Kavita Menon", "Dev Bansal", "Isha Sethi", "Manish Yadav", "Tanya Bose"
    ],
    "department": [
        "IT", "HR", "Finance", "Sales", "Operations",
        "IT", "HR", "Finance", "Sales", "Operations",
        "IT", "HR", "Finance", "Sales", "Operations",
        "IT", "HR", "Finance", "Sales", "Operations"
    ],
    "city": [
        "Pune", "Bengaluru", "Kolkata", "Mumbai", "Hyderabad",
        "Jaipur", "Delhi", "Chennai", "Pune", "Bengaluru",
        "Kolkata", "Mumbai", "Hyderabad", "Jaipur", "Delhi",
        "Chennai", "Pune", "Bengaluru", "Kolkata", "Mumbai"
    ],
    "salary_inr": [
        85000, 88500, 92000, 95500, 99000,
        102500, 106000, 109500, 113000, 116500,
        120000, 123500, 127000, 130500, 134000,
        137500, 141000, 144500, 148000, 151500
    ]
}

manager_df = pd.DataFrame(managers_data)

# Dataset 2: Employees (20 Records)
employees_data = {
    "emp_id": [
        "E001", "E002", "E003", "E004", "E005", "E006", "E007", "E008", "E009", "E010",
        "E011", "E012", "E013", "E014", "E015", "E016", "E017", "E018", "E019", "E020"
    ],
    "employee_name": [
        "Aarav Kumar", "Diya Shah", "Aditya Jain", "Sara Khan", "Rohan Gupta",
        "Ananya Das", "Kabir Sinha", "Ishita Rao", "Varun Nair", "Simran Kaur",
        "Yash Patel", "Nisha Verma", "Harsh Mehta", "Tara Kapoor", "Om Prakash",
        "Riya Sen", "Akash Singh", "Maya Iyer", "Sahil Bansal", "Pallavi Joshi"
    ],
    "department": [
        "IT", "Finance", "Operations", "HR", "Sales",
        "IT", "Finance", "Operations", "HR", "Sales",
        "IT", "Finance", "Operations", "HR", "Sales",
        "IT", "Finance", "Operations", "HR", "Sales"
    ],
    "city": [
        "Delhi", "Jaipur", "Hyderabad", "Mumbai", "Kolkata",
        "Bengaluru", "Pune", "Chennai", "Delhi", "Jaipur",
        "Hyderabad", "Mumbai", "Kolkata", "Bengaluru", "Pune",
        "Chennai", "Delhi", "Jaipur", "Hyderabad", "Mumbai"
    ],
    "manager_id": [
        "M001", "M008", "M015", "M002", "M009",
        "M016", "M003", "M010", "M017", "M004",
        "M011", "M018", "M005", "M012", "M019",
        "M006", "M013", "M020", "M007", "M014"
    ],
    "salary_inr": [
        32000, 33750, 35500, 37250, 39000,
        40750, 42500, 44250, 46000, 47750,
        49500, 51250, 53000, 54750, 56500,
        58250, 60000, 61750, 63500, 65250
    ]
}

# Create employee_df and manager_df using pandas.DataFrame().
employee_df = pd.DataFrame(employees_data)

# print("Managers DataFrame:")
print(manager_df)

# print("Employees DataFrame:")
print(employee_df)


# queries
# Merge both DataFrames on manager_id and display employee name, manager name, employee city and manager city.
df = pd.merge(
    employee_df,
    manager_df,
    on="manager_id",
    suffixes=("_emp", "_mgr")
)
print(df)

# Find employees whose city differs from their manager’s city.
# show employees -> city != managers city
result = df[df["city_mgr"] != df["city_emp"]]
print(result[["emp_id", "employee_name", "city_emp","manager_id", "manager_name", "city_mgr"]])


# Calculate employee count and average salary department-wise.
# result1 = employee_df["emp_id"].count()
result2 = df.groupby("department_mgr").agg(
    employee_count=("emp_id", "count"),
    average_salary=("salary_inr_emp", "mean")
)
print(result2)


# Find the highest-paid employee in each department.
result = df.groupby("department_emp").agg(
    max_salary_each_department=("salary_inr_emp", "max")
)
print(result)


# Calculate the number of employees reporting to each manager.
result = df.groupby("manager_id").agg(
    employee_count_each_manager=("emp_id", "count")
)
print(result)


# 1. Maximum salary from IT department
print("=== Maximum IT Employee Salary ===")
print(df[df["department_emp"] == "IT"]["salary_inr_emp"].max())


# 2. Average salary for all departments
print("\n=== Average Salary Department Wise ===")
print(df.groupby("department_emp").agg(
        average_salary=("salary_inr_emp", "mean")
    )
)


# 3. Managers with salary greater than department average
print("\n=== Managers With Salary Greater Than Department Average ===")

# 4. Employee ID, Employee Name, Manager ID, Manager Name
print("\n=== Employee and Manager Details ===")
print(df[["emp_id","employee_name","manager_id","manager_name"]])


# 5. Manager having maximum employees
print("\n=== Manager With Maximum Employees ===")

result = (
    df.groupby(["manager_id", "manager_name"])
    .agg(employee_count=("emp_id", "count"))
    .sort_values(by="employee_count", ascending=False)
    .head(1)
)
print(result)


# 6. Managers with no employee reporting

# 7. Count of employees + managers department wise

# 8. Department with maximum aggregate salary
print("\n=== Department With Maximum Aggregate Employee Salary ===")

dept_salary = df.groupby("department_emp")["salary_inr_emp"].sum()
print(dept_salary.idxmax())


# 9. Employees whose city differs from manager city
print("\n=== Employees Reporting To Manager In Different City ===")

result = df[df["city_emp"] != df["city_mgr"]][
    [
        "emp_id",
        "employee_name",
        "city_emp",
        "manager_name",
        "city_mgr"
    ]
]

print(result)


# 10. Employees reporting to the same manager
print("\n=== Employees Reporting To Same Manager ===")
