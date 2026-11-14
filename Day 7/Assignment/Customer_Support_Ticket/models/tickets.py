from typing import Literal
from pydantic import BaseModel


class TicketRequest(BaseModel):
    ticket_id: str
    employee_name: str
    department: str
    issue_description: str


class TicketResponse(BaseModel):
    ticket_id: str
    category: str
    priority: Literal["Low", "Medium", "High", "Critical"]
    issue_summary: str
    business_impact: str
    suggested_resolution_steps: list[str]
    recommended_team: str
    escalation_required: bool
    justification: str