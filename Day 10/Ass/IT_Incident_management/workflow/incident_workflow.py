from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from model.incident_model import IncidentRequest
from service.llm_service import analyze_incident


class IncidentState(TypedDict, total=False):
    # input
    employee_id: str
    employee_name: str
    department: str
    issue: str
    # filled by analyze_node
    category: str
    priority: str
    summary: str
    suggested_resolution: str
    # filled by escalate_node / resolve_node
    escalation_required: bool
    email_status: str
    status: str


def analyze_node(state: IncidentState):

    request = IncidentRequest(
        employee_id=state["employee_id"],
        employee_name=state["employee_name"],
        department=state["department"],
        issue=state["issue"],
    )

    result = analyze_incident(request)

    return {
        "category": result.category,
        "priority": result.priority,
        "summary": result.summary,
        "suggested_resolution": result.suggested_resolution,
    }


# Decides which node runs next
def route_by_priority(state: IncidentState) -> str:
    if state["priority"] in ("Critical", "High"):
        return "escalate"
    return "resolve"


def escalate_node(state: IncidentState):
    return {
        "escalation_required": True,
        "email_status": "Email successfully sent",
        "status": "Escalated",
    }


def resolve_node(state: IncidentState):
    return {
        "escalation_required": False,
        "email_status": "Email not required",
        "status": "Resolution suggested",
    }


workflow = StateGraph(IncidentState)

workflow.add_node("analyze_node", analyze_node)
workflow.add_node("escalate_node", escalate_node)
workflow.add_node("resolve_node", resolve_node)

workflow.add_edge(START, "analyze_node")
workflow.add_conditional_edges(
    "analyze_node",
    route_by_priority,
    {"escalate": "escalate_node", "resolve": "resolve_node"},
)
workflow.add_edge("escalate_node", END)
workflow.add_edge("resolve_node", END)

workflow_graph = workflow.compile()