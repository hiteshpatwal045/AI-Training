from fastapi import FastAPI

from model.models import (EmpRequest, EmpResponse)
from service.service import analyze
from workflow.workflows import workflow_graph

app = FastAPI(
    title="AI Employee Leave",
    version="1.1"
)


@app.get("/")
def home():
    return {
        "message": "AI Employee Leave"
    }


@app.get("/health")
def health():
    return {
        "message": "Program is Running UP"
    }


@app.post("/api/v1/anlayzee", response_model=EmpResponse)
def analyze_data_langchain(data: EmpRequest):
    result = analyze(data)
    return result


@app.post("/api/v1/analyzeed", response_model=EmpResponse)
def get_data_langgraph(data: EmpRequest):

    result = workflow_graph.invoke({
        "employee_id": data.employee_id,
        "employee_name": data.employee_name,
        "leave_type": data.leave_type,
        "number_of_days": data.number_of_days,
        "reason": data.reason,
    })

    return result

    # return EmpResponse(
    #     employee_id=result["employee_id"],
    #     summary=result["summary"],
    #     recommendation_action=result["recommendation_action"],
    #     status=result["status"]
    # )
