from pydantic import BaseModel
from typing import Literal


# Model 1: Incoming Leave Request
class LeaveRequest(BaseModel):
  employee_id: int
  employee_name: str
  leave_type: Literal["Sick", "Casual", "Earned", "Other"]
  days_requested: int
  question: str


# Model 2: AI Leave Analysis
class LeaveAnalysis(BaseModel):
  category: Literal["Eligibility", "Procedure", "Documents", "Other"]
  urgency: Literal["Low", "Medium", "High"]
  requires_hr_review: bool
  summary: str


# Model 3: Final Leave Response
class LeaveResponse(BaseModel):
  employee_id: int
  employee_name: str
  analysis: LeaveAnalysis
  guidance: str
  next_step: str
  disclaimer: str
  status: str = "success"
