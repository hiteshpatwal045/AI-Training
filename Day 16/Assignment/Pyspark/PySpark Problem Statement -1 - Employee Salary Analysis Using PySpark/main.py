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

#  Operation 1: Create SparkSession
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
    StructField("department", StringType(), True),
    StructField("city", StringType(), True),
    StructField("salary", DoubleType(), True),
    StructField("experience", IntegerType(), True),
])

# Read the CSV file using PySpark.  
employee_df = spark.read.csv(
    "employees.csv",
    header=True,
    schema=schema,
    mode="FAILFAST"
)


# Display the schema.  
employee_df.printSchema()

# Show all employee records.  
employee_df.show()


# Find employees working in the IT department.  
employee_df.filter(
    (col("department")=="IT")
).show()


# Find employees whose salary is greater than ₹50,000.  
employee_df.filter(
    (col("salary") > 50000)
).show()


# Calculate the average salary of all employees.  
(
    employee_df.agg(
        round(avg("salary"),2).alias("average_salary")
    ).show()
)

# Find the highest-paid employee.  
(
    employee_df
    .agg(max("salary").alias("HighestPaidEmployee"))
    .show()
)


# Count employees department-wise.  
(
    employee_df.groupBy("department")
    .agg(count("employee_id").alias("countEmployee"))
    .show()
)

# Sort employees by salary in descending order.  
(
    employee_df
    .orderBy(desc("salary"))
    .show()
)

# Save the filtered IT employee data into a new CSV file. 

employee_df.toPandas().to_csv(
    "transformed_employees.csv",
    index=False
)
print("Employee data exported successfully")

