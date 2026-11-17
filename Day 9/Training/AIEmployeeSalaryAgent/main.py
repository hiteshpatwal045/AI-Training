from fastapi import FastAPI
from service.llm_service import calculate_employee_salary
from model.ai_model import (SalaryResponse, SalaryRequest)


app = FastAPI(
    title="AI Employee Salary Agent",
    version="1.1"
)


@app.get("/")
def home():
    return {
        "message": "Ai Employee Salary Agent"
    }


@app.post("/api/v1/agent", response_model=SalaryResponse)
def agent_response(request: SalaryRequest):
    return calculate_employee_salary(request)
