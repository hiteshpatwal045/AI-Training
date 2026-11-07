#importing libraries
import pandas as pd
import numpy as np
#Step 2 - Create Panda Series 
salary_series = pd.Series([
    65000, 50000, 72000, 80000, 68000, 90000, 76000
])

print("==================salary_series===============")
print(salary_series)

print("==================Defining Properties================")
#Check properties:
print(salary_series.index)
print(salary_series.values)
print(salary_series.dtype)

#Step 3 - Series with Custom Index
employee_series = pd.Series(
    [
        "Shiv","Athrava","Shreyansh","Sahil",
        "Prince","Hitesh","Akashdeep","Pranjali"
    ],
    index = [
        "E101","E102","E103","E104",
        "E105","E106","E107","E108"
    ]
)

print("==========Series with Custom Index===============")
print(employee_series)
print(employee_series.values)

#Retrieve employees:
print("===========Employee Name with E103===============")
print(employee_series["E103"])
print("===========Employee Name with E106===============")
print(employee_series["E106"])

employee_data = {
    "Employee_ID" : ["E101","E102","E103","E104","E105","E106","E107","E108"],
    "Employee_Name" : ["Shiv","Athrava","Shreyansh","Sahil","Prince","Hitesh","Akashdeep","Pranjali"],
    "Department": ["Sales","HR","Sales","Finance","IT","Sales","IT","Finance"],
    "City": ["Delhi","Mumbai","Pune","Delhi","Mumbai","Bengaluru","Pune","Delhi"],
    "Salary": [65000, 50000, 72000, 80000, 85000, 68000, 90000, 76000],
    "Experience": [5,4,7,8,6,5,9,6],
    "Rating" : [4.5,4.2,4.8,4.6,4.1,4.7,4.9,4.3]
}

print("===============Creat Employee DataFrame=============")
employees_df = pd.DataFrame(employee_data)
print(employees_df)

#Step 5 - Inspect DataFrame
print("==================DataFrame Shapes========================")
print(employees_df.shape)
print(employees_df.columns)
print(employees_df.dtypes)

#step 6 - head()
print("=====First 5 records=====")
print(employees_df.head())

#First 3:
print("=====First 2 records=====")
print(employees_df.head(2))

#Step 6 : tail()
print("==========last 5 Records===============")
print(employees_df.tail())

#Last 2
print("=======Last 2 Records=========")
print(employees_df.tail(2))

print("====Describe=====")
employees_df.info()
print(employees_df.describe())

print("===========selcect 1 column=======")
print(employees_df["Employee_Name"])

print("=========Select multiple Column=======")
print(employees_df[["Employee_Name","Salary"]])

# print("=========Select multiple Column with single list=======")
# print(employees_df["Employee_Name","Salary"])

#Employee Salary > 80,000
result = employees_df["Salary"] > 80000
print(result)

result1 = employees_df[
    employees_df["Salary"] > 80000
]
print(result1)

result2 = employees_df[
    employees_df["Rating"] > 4.5
]
print(result2)

result3 = employees_df[
    employees_df["Department"] == "Sales"
]
print(result3)

delhi_employees = employees_df[
    employees_df["City"] == "Delhi"
]
print(delhi_employees)


print("=============Mulitple Condition on dataframes==============")
multiple_condition = employees_df[
    (employees_df["Rating"] >= 4.5) &
    (employees_df["Salary"] >= 70000)
]
print(multiple_condition)

#first way 
emp_dept_it_finance = employees_df[
    (employees_df["Department"] == "IT") |
    (employees_df["Department"] == "Finance")
]
print(emp_dept_it_finance)

#second_way 
emp_dept_it_finance_way2 = employees_df[
    employees_df["Department"].isin(
        ["IT" ,"Finance"]
    )
]
print(emp_dept_it_finance_way2)

#annual - new Column
employees_df["Annual Salary"] = employees_df["Salary"] * 12
print(employees_df)

#Revised salary - new Column
employees_df["Revised Salary"] = employees_df["Annual Salary"] * 1.08
print(employees_df)

#Bonus salary - new Column
employees_df["Bonus Salary"] = employees_df["Revised Salary"] * 0.05
print(employees_df)

#mothly compensation [Revised salary] + emp[bonus]
employees_df["Monthly Compensation"] = employees_df["Revised Salary"] + employees_df["Bonus Salary"]
print(employees_df)

print("================min,max,sum===============")

#  df["salary"].mean()
print(f"mean of all revised salary : {employees_df["Revised Salary"].mean().sum()}")
emp_rating_mean = employees_df["Rating"].mean()
print(f"Average Rating : {emp_rating_mean}")

#count only unique dept
count_unique_dept = len(employees_df["Department"].value_counts())
print(f"total unique dept using value_count() are : {count_unique_dept}")

#count only all dept
count_all_dept = employees_df["Department"].count()
print(f"total dept : {count_all_dept}")

count_all_dept_2way = employees_df["Department"].nunique()
print(f"total unique dept using nuique() are : {count_all_dept_2way}")

#sorting funciton sort_values()
sort_by_asc = employees_df.sort_values(by="Salary") 
print(sort_by_asc)

#sort by desc
sort_by_desc = employees_df.sort_values(by="Salary",ascending=False)
print(sort_by_desc)

## top 3 highest salary 
top_3_highest_Sal = employees_df.sort_values(by="Salary",ascending=False).head(3);
print(top_3_highest_Sal)

#top 3 Highest Salary 2way with only 1 records
top_3_Highest_sal_no_other_records = employees_df["Salary"].sort_values(ascending=False).head(3);
print(top_3_Highest_sal_no_other_records)


