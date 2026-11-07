from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from config.logging_config import logger
from services import customer_services as service
from models import customer_models as model
from schemas import customer_schemas as schema
from config import database

app = FastAPI(
    title="FastAPI is running",
    version="1.0.1"
)

database.Base.metadata.create_all(bind=database.engine)

# 0. Home PAGE


@app.get("/")
def Home():
    logger.info("Home API Called")
    return {
        "Message": "Fast-API"
    }

# 1. fetch all data


@app.get("/employees", response_model=list[schema.EmployeeResponse])
def getAllEmployees():
    logger.info("Get All Employee Endpoint Called")
    db = database.sessionLocal()

    try:
        customers = service.get_all_employees(db)
        logger.info(f"Successfully Retrieved %s customers {len(customers)}")
        return customers
    finally:
        db.close()

# 2. get by id


@app.get("/employees/{id}", response_model=schema.EmployeeResponse)
def getEmployeeById(id: int):
    logger.info("Get EmployeeId  Endpoint Called")
    db = database.sessionLocal()
    try:
        customer = service.get_employee_by_id(db, id)
        if customer is None:
            raise HTTPException(
                status_code=404,
                detail="customer not found"
            )
        logger.info(f"Successfully Retrieved Customer with ID: ", {id})
        return customer
    finally:
        db.close

# 3. Add/Create Employee


@app.post("/employees", response_model=schema.EmployeeResponse)
def createEmployee(data: schema.EmployeeCreate):
    logger.info("Create Employee Endpoint Called")
    db = database.sessionLocal()
    return service.add_employee(db, data)

# 4. Update Endpoints


@app.put("/employees/{id}")
def updateEmployee(id: int, data: dict):
    updatedData = {}

    updatedData["customer_name"] = data["customer_name"]
    updatedData["age"] = data["age"]
    updatedData["email"] = data["email"]
    updatedData["department"] = data["department"]

    db = database.sessionLocal()
    employee = service.update_empoyee(db, id, updatedData)
    db.close()

    return employee

# 5. Delete Endpoints


@app.delete("/employees/{id}")
def deleteEmployee(id: int):
    logger.info("Delete Endpoint Called")
    db = database.sessionLocal()

    delEmp = service.delete_employee(db, id)

    db.close()
    if not delEmp:
        logger.info(f"Emp with id : %s Already Deleted/ Not Exist", {id})
        return {
            "Result": False,
            "Msg": "Already deleted/ Not Exist"
        }

    logger.info(f"Emp with id : %s Deleted", {id})
    return {
        "Result": True,
        "Msg": "Deleted"
    }
