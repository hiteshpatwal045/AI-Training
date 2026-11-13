import logging

from fastapi import HTTPException

import pandas as pd
# from etl_pipeline import run_etl_pipeline
from model.employee_model import Employee, Payroll
from schema.employee_schema import ETLRunResponse

logger = logging.getLogger("payroll_api")

# list all Employees
def list_employees(db):
  return db.query(Employee).order_by(Employee.employee_id).all()

def get_employee(db, employee_id):
  employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
  if employee is None:
    raise HTTPException(
      status_code=404,
      detail="Employee not found"
    )
  return employee


def create_employee(db, data):
  exists = db.query(Employee).filter(Employee.employee_id == data.employee_id).first()
  if exists:
    raise HTTPException(
      status_code=409,
      detail="Employee ID already exists"
    )

  employee = Employee(**data.model_dump())
  db.add(employee)
  db.commit()
  db.refresh(employee)
  logger.info("Created employee %s", data.employee_id)
  return employee


def update_employee(db, employee_id, data):
  employee = get_employee(db, employee_id)  # raises 404 if missing
  for field, value in data.model_dump(exclude_unset=True).items():
    setattr(employee, field, value)
  db.commit()
  db.refresh(employee)
  logger.info("Updated employee %s", employee_id)
  return employee


def delete_employee(db, employee_id):
  employee = get_employee(db, employee_id)
  db.delete(employee)
  db.commit()
  logger.info("Deleted employee %s", employee_id)


# Payroll

def get_employee_payroll(db, employee_id):
  get_employee(db, employee_id)
  return (
    db.query(Payroll)
    .filter(Payroll.employee_id == employee_id)
    .order_by(Payroll.payroll_month)
    .all()
  )


def load_payroll_df(db):
  query = (
    db.query(
      Employee.employee_id,
      Employee.employee_name,
      Employee.department,
      Payroll.payroll_month,
      Payroll.gross_salary,
      Payroll.net_salary,
      Payroll.deductions,
    )
    .join(Payroll, Payroll.employee_id == Employee.employee_id)
  )
  return pd.read_sql(query.statement, db.get_bind())




# Analytics

def get_department_analysis(db):
  df = load_payroll_df(db)
  return {
    "total_gross": float(df["gross_salary"].sum()),
    "total_net": float(df["net_salary"].sum()),
    "total_deductions": float(df["deductions"].sum()),
    "employee_count": int(df["employee_id"].nunique()),
    "month_count": int(df["payroll_month"].nunique()),
  }


def get_top_earners(db):
  df = load_payroll_df(db)
  return (
    df.groupby(["employee_id", "employee_name", "department"], as_index=False)
      .agg(avg_net_salary=("net_salary", "mean"))
      .round(2)
      .sort_values(by="avg_net_salary", ascending=False)
      .head(10)
      .to_dict("records")
  )


# ETL

def run_etl(db):
  logger.info("ETL Not connected")
  # try:
  #   details = run_etl_pipeline()
  # except Exception as error:
  #   logger.exception("ETL failed")
  #   raise HTTPException(status_code=500, detail=f"ETL failed: {error}")