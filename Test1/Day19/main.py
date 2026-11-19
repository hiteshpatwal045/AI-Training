from fastapi import FastAPI

from model.emp_model import EmpResponse, EmpRequest
from service.emp_service import analyze_output

app = FastAPI(
    title="EMP Feedback AI Analyser",
    version="1.1"
)


@app.get("/")
def homepage():
    return {
        "message": "This is the home page of the EMP Feedback AI analyser"
    }


@app.post("/api/v1/analyze", response_model=EmpResponse)
def analyze(data: EmpRequest):
    return analyze_output(data)
