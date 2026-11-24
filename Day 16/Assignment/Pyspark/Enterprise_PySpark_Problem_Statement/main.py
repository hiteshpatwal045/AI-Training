from pyspark.sql.window import Window
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DoubleType
)

from pyspark.sql.functions import (
    col, sum, avg, max,
    min, count, when, round,
    to_date, row_number, desc, asc,
    max_by, min_by
)
from pyspark.sql import SparkSession

# 1. Create a SparkSession.
spark = (
    SparkSession.builder
    .appName("employee_analytics_main")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

print("Spark started Successfully")


schema = StructType([
    StructField("employee_id", IntegerType(), True),
    StructField("employee_name", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("department", StringType(), True),
    StructField("city", StringType(), True),
    StructField("salary", DoubleType(), True),
    StructField("experience", IntegerType(), True),
    StructField("performance_rating", DoubleType(), True),
])

# 2. Read the employee CSV file into a DataFrame.
employee_df = spark.read.csv(
    "employees.csv",
    header=True,
    schema=schema,
    mode="FAILFAST"
)


# 3. Display the schema.
employee_df.printSchema()

# 4. Display the first 10 records.
employee_df.show()


# Part 2 – Data Exploration

# 5. Count the total number of employees.
(
    employee_df
    .agg(count("employee_id")).alias("count_emp")
    .show()
)

# 6. Display only Employee Name, Department, and Salary.
(
    employee_df.select(
        "employee_name",
        "department",
        "salary")
    .show()
)

# 7. Find all employees working in the IT department.
(
    employee_df.filter(
        (col("department") == "IT")
    ).show()
)

# 8. Find employees earning more than ₹80,000.
(
    employee_df.filter(
        (col("salary") > 80000)
    ).show()
)

# 9. Find employees whose experience is greater than 5 years.
(
    employee_df.filter(
        (col("experience") > 5)
    ).show()
)


# Part 3 – Data Transformation


# 10. Add a new column Annual Salary.
# Formula
# Annual Salary = Salary × 12
employee_df = (
    employee_df.withColumn(
        "annual_salary",
        col("salary") * .12
    )
)
employee_df.select(
    "employee_id",
    "employee_name",
    "annual_salary"
).show(3)


# 11. Add a new Bonus column.
# Business Rule
# Salary > ₹80,000 → Bonus = 15%
# Salary between ₹60,000–₹80,000 → Bonus = 10%
# Otherwise → Bonus = 5%
employee_df = (
    employee_df.withColumn(
        "bonus",
        when(
            col("salary") > 80000,
            col("salary") * .15
        )
        .when(
            col("salary") > 80000,
            col("salary") * .10
        )
        .otherwise(
            col("salary") * .05
        )
    )
)

employee_df.select(
    "employee_id",
    "employee_name",
    "bonus"
).show(3)


# 12. Add a Salary Grade column.
# Example
# A (>₹100,000)
# B (₹80,000–₹100,000)
# C (₹60,000–₹80,000)
# D (<₹60,000)

employee_df = (
    employee_df.withColumn(
        "Grade",
        when(col("salary") > 100000, "A")
        .when(col("salary") > 80000, "B")
        .when(col("salary") > 60000, "C")
        .otherwise("D")
    )
)

employee_df.select(
    "employee_id",
    "employee_name",
    "Grade"
).show(3)


# Part 4 – Sorting

# 13. Sort employees by Salary (Descending).
(
    employee_df.orderBy(desc("salary")).show()
)


# 14. Sort employees by Experience (Ascending).
(
    employee_df.orderBy("experience").show()
)

# Part 5 – Aggregation
# 15. Find

# Maximum Salary
(
    employee_df.agg(
        max("salary").alias("Maximum_Salary")
    ).show()
)


# Minimum Salary

(
    employee_df.agg(
        min("salary").alias("Minimum_Salary")
    ).show()
)


# Average Salary
(
    employee_df.agg(
        round(avg("salary"),2).alias("Average_Salary")
    ).show()
)




# Total Salary


# 16. Count employees department-wise.

(
    employee_df
    .groupBy("department")
    .agg(
        count("employee_id").alias("emp_count")
    ).show()
)


# 17. Calculate average salary department-wise.
(
    employee_df
    .groupBy("department")
    .agg(
        round(avg("salary"),2).alias("average_salary")
    ).show()
)


# 18. Find the highest-paid employee in every department.

(
    employee_df.groupBy("department")
    .agg(
        max("salary").alias("highest_paid")
    ).show()
)


# Part 6 – Advanced Operations

# 19. Filter employees
# Performance Rating > 4
# Experience > 5
# Salary > ₹70,000
# Return only employees satisfying all three conditions.

(
    employee_df.filter(
        (col("performance_rating") > 4) &
        (col("experience") > 5) & 
        (col("salary") > 70000)
    ).show()
)

# 20. Save the final transformed DataFrame into
# # CSV

employee_df.toPandas().to_csv(
    "transformed_employees.csv",
    index=False
)
print("Employee data exported successfully")

