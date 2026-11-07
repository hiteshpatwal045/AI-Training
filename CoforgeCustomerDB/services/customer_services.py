from sqlalchemy import select, func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models.customer_models import Employee


# 1. Add employee
def add_employee(db: Session, data):
    employee = Employee(**data.model_dump())
    db.add(employee)

    try:
        db.commit()
        db.refresh(employee)
        return employee
    except IntegrityError:
        db.rollback()
        raise


# 2. all employee
def get_all_employees(db: Session):

    query = select(Employee).order_by(Employee.customer_id)
    result = db.scalars(query)
    employees = result.all()
    return employees


# 3. search by id
def get_employee_by_id(db: Session, customer_id: int):
    return db.get(Employee, customer_id)


# 4. update
def update_empoyee(db: Session, customer_id: int, data: dict):
    employee = db.get(Employee, customer_id)

    if employee is None:
        return None
    for key, value in data.model_dump().items():
        setattr(employee, key, value)

    try:
        db.commit()
        db.refresh(employee)
        return employee
    except IntegrityError:
        db.rollback()
        raise


# 5. Delete
def delete_employee(db: Session, customer_id: int):
    employee = db.get(Employee, customer_id)

    if employee is None:
        return False
    db.delete(employee)
    db.commit()

    return True
