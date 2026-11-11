from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

from logger import logger

from model.employee_performance_model import EmployeePerformance
from schema.employee_performance_schema import (
  CreateEmployeePerformance,
  UpdateEmployeePerformance,
)

#1. create
def create_employee(db : Session, data : CreateEmployeePerformance):
  new_employee = EmployeePerformance(**data.model_dump())

  try:
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    logger.info("Employee created successfully : ID %s", new_employee.emp_id)
    return new_employee
  except IntegrityError:
    db.rollback()
    logger.warning("Employee creation failed due to an integrity constraint")
    raise HTTPException(
      status_code=409,
      detail="Employee ID already exists"
    )
  except Exception:
    db.rollback()
    logger.exception("Unexpected error while creating employee")
    raise

#2. fetch all data
def get_all_employee(db : Session):
  emp = db.query(EmployeePerformance).all()
  return emp

#3. fetch by id
def get_employee_by_id(db : Session, id : int):
  try:
    emp = db.query(EmployeePerformance).filter(EmployeePerformance.emp_id == id).first()

    if emp is None:
      logger.warning("Employee not found with ID: %s", id)
      raise HTTPException(
        status_code=404,
        detail="Employee Not Found"
      )
    return emp
  except HTTPException:
    raise

  except Exception:
    logger.exception("unexpected error while fetching Employee Id %s", id)
    raise

#4. update data
def update_employee_performance(db : Session, id : int,  data : UpdateEmployeePerformance):
  emp = get_employee_by_id(db, id)

  update_data = data.model_dump(exclude_unset=True)

  if not update_data:
    raise HTTPException(
      status_code=422,
      detail="At least one field must be provided"
    )

  for key, value in update_data.items():
    setattr(emp,key,value)

  try:
    db.commit()
    db.refresh(emp)
    logger.info("Employee updated successfully: ID %s", id)
    return emp
  except Exception:
    db.rollback()
    logger.info("Unexpected error while updating the Employee Id %s", id)
    raise

#5. delete data
def delete_employee(db : Session, id : int):
  emp = get_employee_by_id(db, id)

  try:
    db.delete(emp)
    db.commit()
    logger.info("Employee deleted Successfully: Id %s",id)
    return {"message":"Employee Deleted Successfully"}
  except Exception:
    db.rollback()
    logger.exception("Unexpected error while deleting the Employee with ID: %s", id)
    raise

#6. Filter employees by department.
def get_employees_by_department(db:Session, department : str):
  try:
    emp = db.query(EmployeePerformance).filter(EmployeePerformance.emp_department == department).all()
    return emp
  except Exception:
    logger.exception("Unexpected error while fetching by department")
    raise

#7. Find employees whose performance rating is at least 4.
def get_high_employee(db:Session):
  try:
    emp = db.query(EmployeePerformance).filter(EmployeePerformance.emp_performance_rating >= 4).all()
    return emp
  except Exception:
    logger.exception("Unexpected error while fetching high-performing employees")
    raise

#8. Calculate average performance rating by department.
def get_emp_avg_performance_rating_department(db:Session):
  try:
    emp = db.query(
      EmployeePerformance.emp_department,
      func.avg(EmployeePerformance.emp_performance_rating).label("emp_performance_rating")
      ).group_by(
        EmployeePerformance.emp_department
      ).all()

    return emp
  except Exception:
    logger.exception("Unexpected error while calculating department average ratings")
    raise

#9. Return the five highest-paid employees.
def get_top_five_employee(db:Session):
  try:
    emp = db.query(EmployeePerformance).order_by(
      EmployeePerformance.emp_salary.desc(),
      EmployeePerformance.emp_id.asc()
      ).limit(5).all()

    return emp
  except Exception:
    logger.exception("Unexpected error while fetching the five highest-paid employees")
    raise

#10. Classify employees as Outstanding (4.5 or higher), Good (3.5 to below 4.5), or Needs Improvement (below 3.5).
def get_employee_classification(db:Session):
  try:
    emp = db.query(EmployeePerformance).all()
    result = []

    category = ""

    for e in emp:
      if e.emp_performance_rating >= 4.5:
        category = "Outstanding"
      elif e.emp_performance_rating >= 3.5:
        category = "Good"
      else:
        category = "Needs Improvement"

      result.append({
        "emp_id" : e.emp_id,
        "emp_name" : e.emp_name,
        "emp_rating" : e.emp_performance_rating,
        "category" : category
      })

    return result
  except Exception:
    logger.exception("unexpected error while classifying employees")
    raise
