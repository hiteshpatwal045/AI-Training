from datetime import date
from pydantic import BaseModel


class LeaveRequest(BaseModel):
    employee_name: str
    department: str
    leave_type: str
    start_date: date
    end_date: date
    reason: str


class LeaveResponse(BaseModel):
    employee_name: str
    leave_summary: str
    missing_information: list[str]
    policy_questions: list[str]
    suggested_next_steps: list[str]
    manager_review_required: bool
    recommendation_rationale: str
    status: str