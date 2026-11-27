from testdb import manager_df, employee_df

# print(manager_df.head())
# print(employee_df.head())


merged_df = employee_df.merge(
    manager_df,
    on='manager_id',
    suffixes=('_emp', '_mgr')
)

print(merged_df.head(3))
print(employee_df.head(1))
print(manager_df.head(1))


# Q1
# Display all employees working in the IT department.
print(" =============== 1 =============== ")
result = employee_df[employee_df["department"] == "IT"]
print(result)


# Q2
# Display employees whose salary is greater than ₹50,000.
print(" =============== 2 =============== ")
result = employee_df[employee_df["salary_inr"] > 50000]
print(result)


# Q3
# Display employees from Delhi and Mumbai.
print(" =============== 3 =============== ")
result = employee_df[employee_df["city"].isin(["Delhi", "Mumbai"])]
print(result)

# Q4
# Count employees department-wise.
print(" =============== 4 =============== ")
result = employee_df.groupby("department").agg(
    emp_count=("emp_id", "count"),
).reset_index()
print(result)


# Q5
# Calculate average salary department-wise.
print(" =============== 5 =============== ")
result = employee_df.groupby("department").agg(
    avg_sal=("salary_inr", "mean")
)
print(result)


# Q6
# Find the employee with the highest salary.
print(" =============== 6 =============== ")
get = employee_df.agg(
    highest_saly=("salary_inr", "max")
)
highest_sal = get.loc["highest_saly", "salary_inr"]
result = employee_df[employee_df["salary_inr"] == highest_sal]
result2 = result[["employee_name", "emp_id", "salary_inr"]].reset_index()
print(result2)


# Q7
# Find the employee with the lowest salary.
print(" =============== 7 =============== ")
result = employee_df[employee_df["salary_inr"]
                     == employee_df["salary_inr"].min()]
print(result[["employee_name", "emp_id", "salary_inr"]].reset_index())


# Q8
# Sort employees by salary descending.
print(" =============== 8 =============== ")
result = employee_df.sort_values(by="salary_inr", ascending=False)
print(result)

# Q9
# Find all employees whose name starts with "A".
print(" =============== 9 =============== ")
result = employee_df[employee_df["employee_name"].str.startswith(
    "A", na=False)]
print(result)


# Q10
# Display unique cities from the employees dataframe.
print(" =============== 10 =============== ")
result = employee_df["city"].unique()
print(result)

# Q46
# Return
# employee_name
# manager_name
# department
# employee_salary
# manager_salary

# where:

# employee salary > department average
# manager salary > company manager average
# city differs

# Single chain only.
print(" =============== 46 =============== ")


emp_average_salary = employee_df["salary_inr"].mean()
mgr_average_salary = manager_df["salary_inr"].mean()

result = merged_df[[
    "employee_name", "manager_name",
    "department_emp", "salary_inr_emp", "salary_inr_mgr"]]
result2 = result[
    (merged_df["salary_inr_emp"] > emp_average_salary) &
    (merged_df["salary_inr_mgr"] > mgr_average_salary)
]
print(result2)


# Q47

# Find manager whose team's average salary is highest.
print(" =============== 47 =============== ")

result =(   
    merged_df
    .groupby("manager_name")["salary_inr_emp"]
    .mean()
    .sort_values(ascending=False)
    .head(1)
)
print(result)


# Q48

# Find department-wise:

# highest paid employee
# highest paid manager
# salary gap

# Single chain.




# Q49

# Create manager dashboard:

# team_size
# team_avg_salary
# highest_salary
# lowest_salary
# salary_range
