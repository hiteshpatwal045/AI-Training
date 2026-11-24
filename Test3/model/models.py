from pydantic import BaseModel, Field


class VisitorRequest(BaseModel):
    visitor_id: str
    visitor_name: str
    purpose: str
    employee_name: str
    visit_time: str


class VisitorAnalysis(BaseModel):
    visitor_id: str
    is_office_open: bool
    visitor_category: str
    approval_status:  str
    reason: str


class VisitorResponse(BaseModel):
    visitor_id: str
    visitor_name: str
    status: str
    message: str
    visiting_hours: str
