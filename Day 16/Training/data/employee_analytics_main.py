# import os
# os.environ["HADOOP_HOME"] = r"C:\hadoop"
# os.environ["hadoop.home.dir"] = r"C:\hadoop"

# import os
# print("HADOOP_HOME =", os.environ.get("HADOOP_HOME"))

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
import os

os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["hadoop.home.dir"] = r"C:\hadoop"


# ==========================
# part1 DATA LOADING
# ==========================

# Operation 1: Create SparkSession

spark = (
    SparkSession.builder
    .appName("employee_analytics_main")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

print("Spark started Successfully")


# operation 2 Read Employee CSV

schema = StructType([
    StructField("employee_id", IntegerType(), True),
    StructField("employee_name", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("department", StringType(), True),
    StructField("designation", StringType(), True),
    StructField("city", StringType(), True),
    StructField("salary", DoubleType(), True),
    StructField("experience", IntegerType(), True),
    StructField("joining_date", StringType(), True),
    StructField("performance_rating", DoubleType(), True),
    StructField("employment_status", StringType(), True),
])

employee_df = spark.read.csv(
    "employee_enterprise.csv",
    header=True,
    schema=schema,
    mode="FAILFAST"
)

employee_df = employee_df.withColumn(
    "joining_date",
    to_date(col("joining_date"), "yyy-MM-dd")
)


# Operation 3: Display schema

print("\nOperation 03: Display schema")
employee_df.printSchema()

# # Operation 4: Display first 10 records
# print("\nOperation 04: First 10 Employees")
# employee_df.show(10, truncate=False)

# # ==========================
# # Part 2 DATA LOADING
# # ==========================

# # Operation 5: Total Employee count
# print("\nOperation 05: Total Employee")
# print(employee_df.count())

# # Operation 6: Slect employee_name,Department, Salary
# print("\nOperation 06: select emp_name, department, salary")
# employee_df.select(
#     "employee_name",
#     "department",
#     "salary"
# ).show()


# print("\nOperation 07: IT Employees")
# employee_df.filter(
#     col("department") == "IT"
# ).show()

# print("\nOperation 08: Salary > 80000")
# employee_df.filter(
#     col("salary") > 80000
# ).show()


# print("\nOperation 09: Experience > 5")
# employee_df.filter(
#     col("experience") > 5
# ).show()

# =========================
# Part 3 - Data transformation
# =========================


# print("\nOperation 10: Annual Salary")

# employee_df = employee_df.withColumn(
#     "annual_salary",
#     col("salary") * 12
# )
# employee_df.select(
#     "employee_id",
#     "employee_name",
#     "annual_salary"
# ).show()


# print("\nOperation 11: Bonus Calculation of 5%")
# employee_df = employee_df.withColumn(
#     "bonus",
#     when(
#         col("salary") > 80000,
#         col("salary")*0.15
#     ).when(
#         col("salary") >= 65000,
#         col("salary")*0.10
#     ).otherwise(
#         col("salary")*0.05
#     )
# )

# employee_df.select(
#     "employee_id",
#     "employee_name",
#     "bonus"
# ).show()


# print("\nOperation 12: Grade Calculation")
# employee_df = employee_df.withColumn(
#     "grade",
#     when(col("salary") > 100000,"A")
#     .when(col("salary") >= 80000,"B")
#     .when(col("salary") >= 60000,"C")
#     .otherwise("D")
# )


# employee_df.select(
#     "employee_id",
#     "employee_name",
#     "grade"
# ).show(5)

# =================================
# Part 4 Sorting
# =================================


# print("\nOperation 13: Salary Descending")

# employee_df.orderBy(
#     col("salary").desc()
# ).show(10)


# print("\nOperation 14: Salary Ascending")

# employee_df.orderBy(
#     col("salary").asc()
# ).show(10)

# ==================================
# Part 5 : Aggregation
# ==================================

# print("\nOperation 15: Salary Statistics")
# employee_df.agg(
#     max("salary").alias("maximum_salary"),
#     min("salary").alias("minimum_salary"),
#     round(avg("salary"),2).alias("average_salary"),
#     sum("salary").alias("total_salary")
# ).show()


# print("\nOperation 16: Department Employee Count")

# employee_df.groupBy("department").agg(count("employee_id").alias(
#     "employee_count")).orderBy("department").show(10)

# print("\nOperation 17: Department Average salary")

# (
#     employee_df.groupBy("department")
#     .agg(round(avg("salary"), 2).alias("average_salary"))
#     .orderBy("department").show(10)
# )

# print("\nOperation 18: Highest Paid Employee")

# # Highest Paid employee
# (
#     employee_df.groupBy("department")
#     .agg(
#         max_by("employee_id", "salary").alias("employee_id"),
#         max_by("employee_name", "salary").alias("employee_name"),
#         max("salary").alias("salary")
#     ).show(5)
# )

# print("\nOperation 18: Lowest Paid Employee")

# # Lowest Paid Employee
# (
#     employee_df.groupBy("department")
#     .agg(
#         min_by("employee_id", "salary").alias("employee_id"),
#         min_by("employee_name", "salary").alias("employee_name"),
#         min("salary").alias("salary")
#     ).show(5)
# )


# print("\nOperation 19: Highest Paid Employee sla > 160000")
# (
#     employee_df.groupBy("department")
#     .agg(
#         max_by("employee_id", "salary").alias("employee_id"),
#         max_by("employee_name", "salary").alias("employee_name"),
#         max("salary").alias("salary")
#     ).filter(
#         col("salary") > 160000
#     ).show(5)
# )

# print("\nOperation 20: PerformanceRating > 4, experience > 5 and salary > 70000")

# (
#     employee_df.filter(
#         (col("salary") > 70000) &
#         (col("experience") > 5) &
#         (col("performance_rating") > 4)
#     ).show(5)
# )

# ====================================
# Part 7 Data export
# ====================================

print("\nOperation 20: Exporting CSV")

# (
#     employee_df.write
#     .mode("overwrite")
#     .option("header", True)
#     .csv("output/transformed_employees")
# )
# print("\nOperation 20: Exporting CSV")


employee_df.toPandas().to_csv(
    "output/transformed_employees.csv",
    index=False
)


print("successfully data exported")
