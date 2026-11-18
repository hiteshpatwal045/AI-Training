from fastapi import FastAPI

from model.incident_model import IncidentRequest, IncidentResponse
from workflow.incident_workflow import workflow_graph

app = FastAPI(
    title="AI-Powered IT Incident Management System",
    version="1.1"
)

@app.get("/")
def home():
    return {
        "message":"AI-Powered IT Incident Management System"
    }

@app.post("/api/v1/incident", response_model=IncidentResponse)
def report_incident(data: IncidentRequest):
    result = workflow_graph.invoke({
        "employee_id": data.employee_id,
        "employee_name": data.employee_name,
        "department": data.department,
        "issue": data.issue,
    })

    return IncidentResponse(
        employee_id=result["employee_id"],
        employee_name=result["employee_name"],
        category=result["category"],
        priority=result["priority"],
        summary=result["summary"],
        suggested_resolution=result["suggested_resolution"],
        escalation_required=result["escalation_required"],
        email_status=result["email_status"],
        status=result["status"],
    )