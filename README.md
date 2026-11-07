# AI-Training

A 5-day training program covering Python, data analysis, SQL, REST APIs and ETL. Each day has a `Training` folder (class work) and an `Assignments` folder (exercises).

---

## Day 1 – Python Basics

**Training**
- Taking user input and converting data types
- Area/perimeter, temperature and distance conversions, average marks
- `if / elif / else` (salary bonus, discount calculator, BMI)
- `for` loops, `range()`, `break` and `continue`
- Lists and slicing

**Assignments**
- conditions: employee bonus, loan approval, income tax, insurance premium
- Loop problems: number filtering, amount validation with `while`, vowel/consonant counter, log monitoring

---

## Day 2 – NumPy & Pandas

**Training**
- Pandas Series and DataFrames: head, tail, describe, selecting columns, filtering rows
- Creating new columns, sorting, min/max/sum/mean, top-N records
- NumPy arrays: shape, size, indexing, slicing, standard deviation
- Merging multiple datasets (customers, products, stores, sales)

**Assignments**
- Data files: `HSBC_Synthetic_Banking_Customers.csv`, `coforge_employees_50.xlsx`, `coforge_projects.csv`

---

## Day 3 – MySQL

**Training**
- Create database and table, insert data
- `SELECT`, `WHERE`, `BETWEEN`, `IN`, `LIKE`
- `ORDER BY`, `LIMIT`
- Aggregate functions: `COUNT`, `MIN`, `MAX`, `AVG`, `SUM`
- `GROUP BY` and `HAVING`

**Assignments** (HSBC HR & Payroll database)

contains 3 files with solution of the docx

---

## Day 4 – FastAPI

**Training**
- Building REST APIs with FastAPI, SQLAlchemy, Pydantic and MySQL
- Project structure: `config`, `models`, `schemas`, `services`, `main.py`
- CRUD endpoints (GET, POST, PUT, DELETE), validation, logging, `.env` for database settings
- Two projects: `CoforgeCustomerDB` and `Trainingfeedback`

**Assignment**
- SQL files to create the databases and tables
- 5 API case studies, each with create, list (pagination), get by ID, update and delete:
  Employee Performance, Cricket Player, Training Feedback, Inventory Product, Banking Customer

**FastAPI projects (Day 4)**
------------FastAPI------------

step 1:
----------
python -m venv venv
venv\Scripts\activate

step 2:
----------
pip install fastapi uvicorn python-dotenv pydantic sqlalchemy pymysql pydantic-settings email-validator

step 3:
----------
pip freeze > requirements.txt

step 4:
----------
type nul > database.py

step 5:
----------
type nul > customer_models.py

step 6:
----------
type nul > customer_schemas.py

step 7:
----------
type nul > customer_services.py

step 8:
----------
type nul > main.py

step 9:
----------
uvicorn main:app --reload


---

## Day 5 – ETL Pipeline

**Training** (`ecommerce_etl_pipeline`)
- **Extract** – read `customers`, `orders`, `payments`, `deliveries` CSV files
- **Transform** – remove duplicates, fill missing values, fix text and date formats, calculate total amount
- **Join** – combine all four datasets
- **Report** – total orders and total revenue

---
