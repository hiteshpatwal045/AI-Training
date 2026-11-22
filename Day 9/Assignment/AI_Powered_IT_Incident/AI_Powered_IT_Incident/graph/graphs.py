from typing import Optional, TypedDict

from langgraph.graph import StateGraph, START, END

from model.models import IncidentRequest, IncidentAnalysis
from service.services import analyze_incident


# ---------- State shared by all nodes ----------
class IncidentState(TypedDict):
  employee_id: str
  employee_name: str
  department: str
  issue: str
  analysis: Optional[IncidentAnalysis]
  escalation_required: bool
  status: str


# ---------- Nodes ----------
def analyze_node(state: IncidentState) -> dict:
  request = IncidentRequest(
    employee_id=state["employee_id"],
    employee_name=state["employee_name"],
    department=state["department"],
    issue=state["issue"],
  )
  analysis = analyze_incident(request)
  return {"analysis": analysis}


def escalate_node(state: IncidentState) -> dict:
  return {
    "escalation_required": True,
    "status": "Escalated",
  }


def resolve_node(state: IncidentState) -> dict:
  return {
    "escalation_required": False,
    "status": "Resolution Provided",
  }


# ---------- Conditional function ----------
def route_by_priority(state: IncidentState) -> str:
  if state["analysis"].priority in ("Critical", "High"):
    return "escalate"
  return "resolve"

builder = StateGraph(IncidentState)

builder.add_node("analyze", analyze_node)
builder.add_node("escalate", escalate_node)
builder.add_node("resolve", resolve_node)

builder.add_edge(START, "analyze")
builder.add_conditional_edges(
  "analyze",
  route_by_priority,
  {
    "escalate": "escalate",
    "resolve": "resolve",
  },
)
builder.add_edge("escalate", END)
builder.add_edge("resolve", END)

incident_graph = builder.compile()