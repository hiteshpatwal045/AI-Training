from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from datetime import datetime


from service.services import analyze_data1
from model.models import (
    VisitorAnalysis,
    VisitorResponse,
    VisitorRequest
)


class StateField(TypedDict):
    visitor_id: str
    visitor_name: str
    purpose: str
    employee_name: str
    visit_time: str

    is_office_open: bool
    visitor_category: str
    approval_status:  str
    reason: str

    status: str
    message: str
    visiting_hours: str


def analyzeedata(data: VisitorRequest):
    request = VisitorRequest(
        visitor_id=data.visitor_id,
        visitor_name=data.visitor_name,
        purpose=data.purpose,
        employee_name=data.employee_name,
        visit_time=data.visit_time
    )
    analysis = analyze_data1(request)

    return {
        "is_office_open": analysis["is_office_open"],
        "visitor_category": analysis["visitor_category"],
        "approval_status": analysis["approval_status"],
        "reason": analysis["reason"]
    }


def Conditional_visitor(state: StateField):
    if state["visit_time"] < and state["visit_time"] > :
        return "Allow_Visitor"
    return "Reject_Visitor"


def Allow_Visitor(state: StateField):
    return {
        state["approval_status"]: "Approved"
    }


def Reject_Visitor(state: StateField):
    return {
        state["approval_status"]: "Declined"
    }


workflow = StateGraph(StateField)

workflow.add_node("start",)
