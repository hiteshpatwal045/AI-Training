import os
import sys

python_path = sys.executable
print("Python used by script:", python_path)

os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import when

spark = (
    SparkSession.builder
    .appName("Employee Analysis")
    .master("local[1]")
    .getOrCreate()
)

print("Spark application started successfully")

employee_data = [
    (101,"Shreyansh","IT",50000,"Noida"),
    (102,"Prince","HR",40000,"Delhi"),
    (103,"Hitesh","Finance",45000,"Gurugram"),
    (104,"Sahil","IT",50000,"Pune"),
    (105,"Pranjali","Sales",50000,"Delhi"),
    (106,"Akash","IT",88000,"Noida"),
    (107,"Shivranjan","HR",55000,"Mumbai")
]

columns = [
    "employee_id",
    "employee_name",
    "department",
    "salary",
    "city"
]

employee_df = spark.createDataFrame(employee_data, columns)
# employee_df.show()



# employee_df.select(
#     "employee_name",
#     "department",
#     "salary"
# ).show()


# employee_df.show(3)
# employee_df.show(truncate=False)
# first_employee = employee_df.first()
# print(first_employee)
# employee_df.show(1)

# employee_df.limit(1).show()


# print(first_employee["employee_name"])
# print(first_employee["department"])
# print(first_employee["salary"])

#Total Salary
# employee_df.select(F.show("salary")).show()
# employee_df.select(col("employee_name"),col("salary")).show()

# filter
# employee_df.filter(
#     col("department") == "IT"
# ).show()

# employee_df.filter(
#     col("salary") > 45000
# ).show()



# employee_df.filter(
#     (col("salary") > 50000) &
#     (col("department") == "IT")
# ).show()

# employee_df.filter((
#         (col("city") == "Noida") |
#         (col("city") == "Pune")
#     )  & (
#         (col("department") == "Finance") |
#         (col("department") == "IT")
#     )
# ).show()


# employee_df.withColumn(
#     "annual_salary",
#     col("salary") * 12
# ).show()


# employee_df.withColumn(
#     "bonus",
#     col("salary") * 0.10
# ).show()


# conditional using when

employee_df = employee_df.withColumn(
    "salary_category",
    when(col("salary") >= 50000, "High")
    .otherwise("Standard")
).show()

spark.stop()