from fastapi import Depends, FastAPI

from config.database import Base, engine, get_db
from schema.employee_schema import (
  DepartmentStats, EmployeeCreate, EmployeeOut, EmployeeUpdate,
  ETLRunResponse, PayrollOut, PayrollSummary, TopEarner,
)
from service import employee_service

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Payroll Flow API")


# Employees

@app.get("/employees", response_model=list[EmployeeOut])
def list_employees(db=Depends(get_db)):
  return employee_service.list_employees(db)


@app.get("/employees/{employee_id}", response_model=EmployeeOut)
def get_employee(employee_id: str, db=Depends(get_db)):
  return employee_service.get_employee(db, employee_id)


@app.post("/employees", response_model=EmployeeOut)
def create_employee(data: EmployeeCreate, db=Depends(get_db)):
  return employee_service.create_employee(db, data)


@app.put("/employees/{employee_id}", response_model=EmployeeOut)
def update_employee(employee_id: str, data: EmployeeUpdate, db=Depends(get_db)):
  return employee_service.update_employee(db, employee_id, data)


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: str, db=Depends(get_db)):
  employee_service.delete_employee(db, employee_id)


# Payroll
# "/payroll/summary" must come BEFORE "/payroll/{employee_id}",
# otherwise FastAPI treats the word "summary" as an employee_id.

@app.get("/payroll/summary", response_model=PayrollSummary)
def payroll_summary(db=Depends(get_db)):
  return employee_service.get_payroll_summary(db)


@app.get("/payroll/{employee_id}", response_model=list[PayrollOut])
def employee_payroll(employee_id: str, db=Depends(get_db)):
  return employee_service.get_employee_payroll(db, employee_id)


# Analytics (these use pandas inside the service)

@app.get("/analytics/departments", response_model=list[DepartmentStats])
def department_analysis(db=Depends(get_db)):
  return employee_service.get_department_analysis(db)


@app.get("/analytics/top-earners", response_model=list[TopEarner])
def top_earners(db=Depends(get_db)):
  return employee_service.get_top_earners(db)


# ETL

@app.post("/etl/run", response_model=ETLRunResponse)
def run_etl(db=Depends(get_db)):
  return employee_service.run_etl(db)