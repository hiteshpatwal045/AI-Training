from fastapi import FastAPI

from services import employee_service as service
from config.database import Base, engine, SessionLocal
from schemas.employee_schema import EmployeeResponse, EmployeeCreate
from models.employee_model import Employee

app = FastAPI(
    title="FastAPI is running",
    version="1.0.1"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def Home():
    return{
        "message" : "Fast-API"
    }

#1. fetch all employees
@app.get("/employees",response_model=list[EmployeeResponse])
def getAllEmployees():
    db = SessionLocal()
    return service.get_all_employees(db)

#2. get by employees ID
@app.get("/employees/{id}", response_model=EmployeeResponse)
def getEmployeesById(id: int):
    db = SessionLocal()
    return service.get_employee_by_id(db,id)


 