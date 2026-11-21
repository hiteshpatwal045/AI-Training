from langgraph.graph import StateGraph, START, END
from typing import TypedDict

from model.models import (EmpRequest)
from service.service import analyze


class EmpState(TypedDict):
    employee_id: str
    employee_name: str
    leave_type: str
    number_of_days: int
    reason: str
    summary: str
    recommendation_action: str
    status: str


def analyzing_data(state: EmpState):

    request = EmpRequest(
        employee_id=state["employee_id"],
        employee_name=state["employee_name"],
        leave_type=state["leave_type"],
        number_of_days=state["number_of_days"],
        reason=state["reason"]
    )

    response = analyze(request)

    return {
        "employee_id": response.employee_id,
        "summary": response.summary,
        "recommendation_action": response.recommendation_action,
        "status": response.status
    }


def validate_node(state: EmpState):
    if state["number_of_days"] > 15:
        return {"status": "Denied"}
    return {"status": "Processed"}


def recommend_action(state: EmpState):
    if state["status"] == "Processed":
        return {"recommendation_action": "Approved"}
    return {"recommendation_action": "Not Approved"}


workflow = StateGraph(EmpState)

# nodes are added
workflow.add_node("analyzing_data", analyzing_data)
workflow.add_node("validate_node", validate_node)
workflow.add_node("recommend_action", recommend_action)


# adding the edges
workflow.add_edge(START, "analyzing_data")
workflow.add_edge("analyzing_data", "validate_node")
workflow.add_edge("validate_node", "recommend_action")
workflow.add_edge("recommend_action", END)

workflow_graph = workflow.compile()
