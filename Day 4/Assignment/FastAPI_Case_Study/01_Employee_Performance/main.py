from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from config.database import Base,engine,get_db
from schema.employee_performance_schema import (
  CreateEmployeePerformance,
  UpdateEmployeePerformance,
  ResponseEmployeePerformance,
  DepartmentAverageResponse,
  EmployeeClassificationResponse
)
from service import employee_performance_service as service

Base.metadata.create_all(bind=engine)

app = FastAPI(title = "Employee Performance API")

# 1. create endpoint
@app.post("/employees",response_model=ResponseEmployeePerformance)
def create_emp(data : CreateEmployeePerformance, db : Session = Depends(get_db)):
  return service.create_employee(db,data)

# 2. fetch all emp
@app.get("/employees",response_model=list[ResponseEmployeePerformance])
def fetch_all(db : Session = Depends(get_db)):
  return service.get_all_employee(db)

# 7. get emp with rating >= 4
@app.get("/employees/high-performer",response_model=list[ResponseEmployeePerformance])
def get_emp_by_rating_higher_than_4(db : Session = Depends(get_db)):
  return service.get_high_employee(db)

# 8. calculate average performance rating by department
@app.get("/employees/department/avg-performance",response_model=list[DepartmentAverageResponse])
def get_emp_average_performance_rating_by_department(db : Session = Depends(get_db)):
  return service.get_emp_avg_performance_rating_department(db)

# 9. 5 highest paid emp
@app.get("/employees/department/highest-paid",response_model=list[ResponseEmployeePerformance])
def get_highest_paid_emp(db : Session = Depends(get_db)):
  return service.get_top_five_employee(db)

# 10. classify emp
@app.get("/employees/classify",response_model=list[EmployeeClassificationResponse])
def get_classified_emp(db : Session = Depends(get_db)):
  return service.get_employee_classification(db)

# 3. get emp by id
@app.get("/employees/{id}",response_model=ResponseEmployeePerformance)
def get_emp_by_id( id : int, db : Session = Depends(get_db)):
  return service.get_employee_by_id(db,id)

# 4. update emp
@app.patch("/employees/{id}",response_model=ResponseEmployeePerformance)
def update_emp(id : int, data : UpdateEmployeePerformance, db : Session = Depends(get_db)):
  return service.update_employee_performance(db,id,data)

# 5. delete emp
@app.delete("/employees/{id}")
def delete_emp(id : int, db : Session = Depends(get_db)):
  return service.delete_employee(db,id)

# 6. get emp by department
@app.get("/employees/department/{department}",response_model=list[ResponseEmployeePerformance])
def get_emp_by_department(department : str, db : Session = Depends(get_db)):
  return service.get_employees_by_department(db,department)