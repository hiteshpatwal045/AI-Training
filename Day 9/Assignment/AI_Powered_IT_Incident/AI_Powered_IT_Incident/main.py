from fastapi import FastAPI

from model.models import IncidentRequest, IncidentResponse
from graph.graphs import incident_graph

app = FastAPI(
  title="AI IT Incident Management System",
  version="1.0"
)


@app.get("/")
def home():
  return {
    "message": "Welcome to the AI IT Incident Management System",
    "application": "AI IT Incident Management System"
  }


@app.get("/health")
def health():
  return {"status": "healthy"}


@app.post("/incident/analyze", response_model=IncidentResponse)
def incident_analyze(data: IncidentRequest):
  final_state = incident_graph.invoke({
      "employee_id": data.employee_id,
      "employee_name": data.employee_name,
      "department": data.department,
      "issue": data.issue,
    }
  )

  analysis = final_state["analysis"]

  return IncidentResponse(
    employee_id=data.employee_id,
    employee_name=data.employee_name,
    category=analysis.category,
    priority=analysis.priority,
    summary=analysis.summary,
    suggested_resolution=analysis.suggested_resolution,
    escalation_required=final_state["escalation_required"],
    status=final_state["status"],
  )