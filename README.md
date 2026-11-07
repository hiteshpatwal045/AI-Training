# AI-Training

# AI Training

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
- Business rules using conditions: employee bonus, loan approval, income tax, insurance premium
- Loop problems: number filtering, amount validation with `while`, vowel/consonant counter, log monitoring

---

## Day 2 – NumPy & Pandas

**Training**
- Pandas Series and DataFrames: head, tail, describe, selecting columns, filtering rows
- Creating new columns, sorting, min/max/sum/mean, top-N records
- NumPy arrays: shape, size, indexing, slicing, standard deviation
- Merging multiple datasets (customers, products, stores, sales)

**Assignments**
- **HSBC Banking Analytics** – 40 questions using NumPy and Pandas (statistics, filtering, groupby, pivot table, branch summary)
- **Coforge Employee Analytics** – 50 questions (groupby, joins, ranking, outliers, department scorecard)
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
- `File1` – creates the database and 5 tables (Departments, Employees, Payroll, Projects, EmployeeProjects)
- `File2` – inserts sample data
- `File3` – 96 queries including joins, subqueries and CTEs
- `HSBC_Bank_MySQL_Coforge.docx` – case study document

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

---

## Day 5 – ETL Pipeline

**Training** (`ecommerce_etl_pipeline`)
- **Extract** – read `customers`, `orders`, `payments`, `deliveries` CSV files
- **Transform** – remove duplicates, fill missing values, fix text and date formats, calculate total amount
- **Join** – combine all four datasets
- **Report** – total orders and total revenue (successful payments only)

---

**FastAPI projects (Day 4)**
1. Create the database using the SQL files.
2. Add a `.env` file in the project folder:
   ```env
   DB_HOST=localhost
   DB_PORT=3306
   DB_USERNAME=your_user
   DB_PASSWORD=your_password
   DB_DATABASE=your_database
   ```
3. Install and start:
   ```bash
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```
4. Open `http://127.0.0.1:8000/docs` to test the APIs.

**ETL pipeline (Day 5)**
```bash
pip install -r requirements.txt
python etl_pipeline.py
```
