from pydantic import BaseModel
from typing import Literal


class IncidentRequest(BaseModel):
    employee_id: str
    employee_name: str
    department: str
    issue: str


class IncidentResponse(BaseModel):
    employee_id: str
    employee_name: str
    category: str
    priority: Literal["Critical", "High", "Medium", "Low"]
    summary: str
    suggested_resolution: str
    escalation_required: bool
    email_status: str
    status: str