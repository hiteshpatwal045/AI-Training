import pandas as pd
import numpy as np

df1 = pd.read_csv("data/employees/finance_employees.csv")
df2 = pd.read_csv("data/employees/hr_employees.csv")
df3 = pd.read_csv("data/employees/it_employees.csv")
df4 = pd.read_csv("data/employees/operations_employees.csv")
df5 = pd.read_csv("data/employees/sales_employees.csv")


print(df1.head(3))
print(df2.head(3))
print(df3.head(3))
print(df4.head(3))
print(df5.head(3))


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


# result = employee_df[employee_df["department"] == "Finance"]
print("====== Find employees working in the Finance department =====")
result = employee_df.query("department == 'Finance'")
print(result)


print("======  Display employees whose salary is greater than ₹100,000. =====")
result = employee_df[employee_df["salary"] > 100000]["emp_name"]
print(result)

print("====== Find employees earning between ₹50,000 and ₹90,000.  =====")
result = employee_df[
    (employee_df["salary"] > 50000) &
    (employee_df["salary"] < 90000)
]["emp_name"]
print(result)

print("====== Display all employees located in Pune. =====")
result = employee_df[employee_df["city"] == "Pune"][["emp_name", "city"]]
print(result)

print("====== Q16. Find employees working in IT and located in Bangalore.  =====")
result = employee_df[(employee_df["city"] == "Bangalore")
                     & (employee_df["department"] == "IT")]
print(result)


print("====== Q17. Display Finance employees earning more than ₹80,000 =====")
result = employee_df[(employee_df["department"] == "Finance")
                     & (employee_df["salary"] > 80000)]
print(result)

print("====== Q18. Find employees belonging to either HR or Sales.  =====")
reuslt = employee_df[(employee_df["department"] == "HR")
                     | (employee_df["department"] == "Sales")]
print(result)


print("======  Q19. Display employees whose salary is less than ₹40,000 and who work in Chennai. =====")
result = employee_df[(employee_df["salary"] < 40000) &
                     (employee_df["city"] == "Chennai")]
print(result)


print("====== Q20. Find all employees whose city is not Mumbai =====")
result = employee_df[employee_df["city"] != "Mumbai"]
print(result)


print("====== Q21. Calculate the total salary expenditure across all five departments =====")
result = employee_df["salary"].sum()
print(result)


print("====== Q22. Calculate the total salary paid to IT employees.  ======")
result = employee_df[employee_df["department"] == "IT"]["salary"].sum()
print(result)


print("====== Q23. Calculate the total salary paid to HR employees.  ======")
result = employee_df[employee_df["department"] == "HR"]["salary"].sum()
print(result)


print("====== Q23. Calculate the total salary paid to Finance employees.  ======")
result = employee_df[employee_df["department"] == "Finance"]["salary"].sum()
print(result)


print("====== Q23. Calculate the total salary paid to Sales employees.  ======")
result = employee_df[employee_df["department"] == "Sales"]["salary"].sum()
print(result)


print("====== Q23. Calculate the total salary paid to Operations employees.  ======")
result = employee_df[employee_df["department"] == "Operations"]["salary"].sum()
print(result)

print("====== Q27. Calculate department-wise total salary expenditure using groupby().  ======")
result = employee_df.groupby("department")["salary"].sum()
print(result)

print("====== Q28. Calculate city-wise total salary expenditure.  ======")
result = employee_df.groupby("city")["salary"].sum()
print(result)


print("====== Q29. Find the combined salary expenditure for IT and Finance.  ======")
result = employee_df[(employee_df["department"] == "IT") | (
    employee_df["city"] == "Finance")]["salary"].sum()
print(result)


print("====== Q30. Calculate each department's percentage contribution to the company's total salary expenditure.  ======")
result1 = employee_df["salary"].sum()
result = employee_df.groupby("department")["salary"].sum() / result1 * 100
print(result)


print("====== Q31. Find the maximum salary across the company.  ======")
result = employee_df["salary"].max()
print(result)


print("====== Q32. Find the minimum salary across the company.  ======")
result = employee_df["salary"].min()
print(result)


print("====== Q33. Calculate the average salary of all employees.  ======")
result = employee_df["salary"].mean()
print(result)


print("====== Q34. Find the maximum salary in each department.  ======")
result = employee_df.groupby("department")[["emp_id", "salary"]].agg("max")
print(result)


print("====== Q35. Find the minimum salary in each department.  ======")
result = employee_df.groupby("department")[["emp_id", "salary"]].agg("min")
print(result)


print("====== Q36. Calculate the average salary in each department.  ======")
result = employee_df.groupby("department")[["emp_id", "salary"]].agg("mean")
print(result)


print("====== Q37. Find the maximum salary in each city.  ======")
result = employee_df.groupby("city")[["emp_id", "salary"]].agg("max")
print(result)


print("====== Q38. Find the minimum salary in each city.  ======")
result = employee_df.groupby("city")[["emp_id", "salary"]].agg("min")
print(result)

print("====== Q39. Calculate the average salary for employees in Pune.  ======")
result = employee_df[employee_df["city"] == "Pune"]["salary"].agg("mean")
print(result)

print("====== Q40. Find the difference between maximum and minimum salary for every department.  ======")
result = employee_df.groupby("department")["salary"].agg(["min", "max"])
result["difference"] = result["max"] - result["min"]
print(result)


# Q41. Group employees by department and calculate employee count.
print("====== 41 ======")


# Q42. Group employees by city and calculate employee count.
print("====== 42 ======")


# Q43. Group by department and calculate total salary, average salary, minimum salary and maximum salary in one DataFrame.
print("====== 43 ======")
print("====== 44 ======")
print("====== 45 ======")
print("====== 46 ======")
print("====== 47 ======")
print("====== 48 ======")
print("====== 49 ======")
print("====== 50 ======")
print("====== 44 ======")
print("====== 45 ======")
print("====== 46 ======")
print("====== 47 ======")
print("====== 48 ======")
print("====== 49 ======")
print("====== 50 ======")


# Q44. Group by department and city and calculate total salary.
print("====== 44 ======")
result = employee_df.groupby(["department", "city"])["salary"].sum()
print(result)


# Q45. Group by department and city and calculate average salary.
print("====== 45 ======")
result = employee_df.groupby(["department", "city"])["salary"].mean()
print(result)


# Q46. Group by department and city and calculate employee count.
print("====== 46 ======")
result = employee_df.groupby(["department", "city"])["emp_id"].count()
print(result)


# Q47. Find the department with the highest total salary expenditure.
print("====== 47 ======")
result = employee_df.groupby("department")["salary"].max().idxmax()
print(result)


# Q48. Find the department with the lowest average salary.
print("====== 48 ======")
result = employee_df.groupby("department")["salary"].mean().idxmin()
print(result)


# Q49. Find the city with the highest number of employees.
print("====== 49 ======")
result = employee_df.groupby("city")["emp_id"].count().idxmax()
print(result)


# Q50. Create a department-wise salary summary sorted by total salary in descending order.
print("====== 50 ======")
result = employee_df.groupby("department")[
    "salary"].sum().sort_values(ascending=False)
print(result)


# Q51. Find departments whose total salary expenditure exceeds ₹10,000,000.
print("====== 51 ======")
result = employee_df.groupby("department")["salary"].sum()
result = result[result > 10000000]
print(result)


# Q52. Find departments whose average salary exceeds ₹90,000.
print("====== 52 ======")
result = employee_df.groupby("department")["salary"].mean()
result = result[result > 90000]
print(result)


# Q53. Find departments whose minimum salary is greater than ₹25,000.
print("====== 53 ======")
result = employee_df.groupby("department")["salary"].min()

result = result[result > 25000]

print(result)

# Q54. Find departments whose maximum salary exceeds ₹140,000.
print("====== 54  ======")
result = employee_df.groupby("department")["salary"].max()
result = result[result > 140000]
print(result)

# Q55. Find cities where the total salary expenditure exceeds ₹15,000,000.
print("====== 55  ======")
result = employee_df.groupby("city")["salary"].sum()
print(result[result > 15000000])

# Q56. Find department-city combinations whose average salary exceeds ₹100,000.
print("====== 56 ======")
result = employee_df.groupby(["department", "city"])["salary"].mean()
result = result[result > 100000]
print(result)

# Q57. Find departments having more than 150 employees.
print("======  57  ======")
result = employee_df.groupby("department")["emp_id"].count()
print(result[result > 150])


# Q58. Find cities having more than 100 employees.
print("====== 58 ======")
result = employee_df.groupby("city")["emp_id"].count()
print(result[result > 100])

# Q59. Find department-city combinations whose total salary exceeds ₹3,000,000.
print("====== 59 ======")
result = employee_df.groupby(["department", "city"])["salary"].sum()
print(result[result > 3000000])


# Q60. Find departments whose average salary is greater than the overall company average salary.
print("====== 60 ======")
result1 = employee_df["salary"].mean()
result2 = employee_df.groupby("department")["salary"].mean()
print(result2[result2 > result1])


# Q61. Create a department-wise summary containing total salary, average salary, maximum salary, minimum salary and employee count.
print("====== 61 ======")
result = employee_df.groupby("department")["salary"].agg(
    total_salary="sum",
    average_salary="mean",
    maximum_salary="max",
    minimum_salary="min",
    employee_count="count"
)
print(result)

# Q62. Create a city-wise summary containing total salary, average salary and employee count.
print("====== 62 ======")
result = employee_df.groupby("city")["salary"].agg(["count", "mean", "sum"])
print(result)


# Q63. Calculate the salary range (maximum minus minimum) for every department.
print("====== 63 ======")                                                                                                   
result = employee_df.groupby("department")["salary"].agg(["max", "min"])
result["Range"] = result["max"] - result["min"]
print(result["Range"])


# Q64. Calculate the salary standard deviation for each department.
print("====== 64 ======")
result = employee_df.groupby("department")["salary"].std()
print(result)

# Q65. Calculate the median salary for each department.
print("====== 65 ======")
result = employee_df.groupby("department")["salary"].median()
print(result)

# Q66. Calculate the 25th and 75th salary percentiles for each department.
print("======  ======")
result = employee_df.groupby("department")["salary"].quantile([0.25, 0.75])
print(result)


# Q67. Find the top three departments by average salary.
print("====== 67 ======")
result = employee_df.groupby("department")["salary"].mean()
print(result.sort_values(ascending=False).head(3))

# Q68. Find the top three cities by total salary expenditure.
print("====== 68 ======")
result = employee_df.groupby("city")["salary"].sum()
print(result.sort_values(ascending=False).head(3))

# Q69. Find the department-city combination with the highest average salary.
print("====== 69 ======")
result = employee_df.groupby(["department", "city"])["salary"].mean().idxmax()
print(result)

# Q70. Calculate each department's share of total employees and total company salary
print("====== 70 ======")

total_employees = employee_df["emp_id"].count()
total_salary = employee_df["salary"].sum()
result = employee_df.groupby("department").agg(
    employee_count=("emp_id", "count"),
    salary_sum=("salary", "sum")
)
result["employee_share"] = result["employee_count"] / total_employees * 100
result["salary_share"] = result["salary_sum"] / total_salary * 100
print(result)


# Q71. Create a department salary summary DataFrame and merge it with employee_df using department.
print("====== 71 ======")
dept_summary = employee_df.groupby("department")["salary"].sum().reset_index()
result = pd.merge(employee_df, dept_summary, on="department")
print(result)


# Q72. Create a city salary summary DataFrame and merge it with employee_df using city.
print("====== 72 ======")
city = employee_df.groupby("city")["salary"].sum().reset_index()
result = pd.merge(employee_df, city, on="city")
print(result)


# Q73. Create a department employee-count DataFrame and merge it with employee_df.
print("====== 73 ======")
result = employee_df.groupby("department")["emp_id"].count().reset_index()
result2 = pd.merge(employee_df, result, on="department")
print(result2)


# Q74. Create a department average-salary DataFrame and merge it with employee_df.
print("====== 74 ======")
avg_salary = employee_df.groupby("department")["salary"].mean().reset_index()
result = pd.merge(employee_df, avg_salary, on="department")
print(result)

# Q75. After merging department averages, find employees earning more than their department's average salary.
print("====== 75 ======")
avg_salary = employee_df.groupby("department")["salary"].transform("mean")
result = employee_df[employee_df["salary"] > avg_salary]
print(result)


# Q76. After merging city averages, find employees earning less than their city's average salary.
print("====== 76 ======")
city_avg = employee_df.groupby("city")["salary"].mean().reset_index()
result = pd.merge(employee_df, city_avg, on="city")
result = result[result["salary_x"] < result["salary_y"]]
print(result)

# Q77. Create separate department salary-total and employee-count summary DataFrames and merge them.
print("====== 77 ======")
dep_sal = employee_df.groupby("department")["salary"].sum().reset_index()
dep_sal = employee_df.groupby("department")["emp_id"].count().reset_index()
result = pd.merge(dep_sal, employee_df, on="department")
print(result)

# Q78. Merge department maximum-salary data with employee_df and identify employees earning the department maximum.
print("====== 78 ======")

max_salary = employee_df.groupby("department")["salary"].max().reset_index()
result = pd.merge(employee_df, max_salary, on="department")
result = result[result["salary_x"] == result["salary_y"]]
print(result)

# Q79. Create department-city salary and employee-count summaries and merge them using both department and city.
print("====== 79 ======")
dep_city_sal = employee_df.groupby(["department", "city"])["salary"].sum().reset_index()
dep_city_emp = employee_df.groupby(["department", "city"])["emp_id"].count().reset_index()
result = pd.merge(dep_city_sal,dep_city_emp,on=["department", "city"])
print(result)

# Q80. Demonstrate inner, left, right and outer joins using a department summary and a department reference DataFrame constructed from the existing data.
print("====== 80 ======")

dept_summary = employee_df.groupby("department")["salary"].sum().reset_index()
dept_ref = pd.DataFrame({"department": ["IT", "HR", "Finance", "Sales", "Operations", "Legal"]})
inner_join = pd.merge(dept_summary, dept_ref, on="department", how="inner")
left_join = pd.merge(dept_summary, dept_ref, on="department", how="left")
right_join = pd.merge(dept_summary, dept_ref, on="department", how="right")
outer_join = pd.merge(dept_summary, dept_ref, on="department", how="outer")

print(inner_join)
print(left_join)
print(right_join)
print(outer_join)

print("======  ======")
