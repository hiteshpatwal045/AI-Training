from fastapi import FastAPI
from service.emp_service import analyze_employee
from models.emp_models import EmployeeRequest, EmployeeResponse

app = FastAPI(
    title="Employee Performance Feedback AI",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "AI Text Assistant is working"
    }


@app.post("/api/v1/analyze-employee", response_model=EmployeeResponse)
def analyze(data: EmployeeRequest):
    return analyze_employee(data)