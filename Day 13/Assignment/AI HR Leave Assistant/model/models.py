from typing import Literal
from pydantic import BaseModel, Field


class LeaveRequest(BaseModel):
  employee_id: int = Field(gt=0)
  employee_name: str = Field(min_length=2)
  leave_type: Literal["Sick", "Casual", "Earned", "Other"]
  days_requested: int = Field(gt=0)
  question: str = Field(min_length=10)


class LeaveAnalysis(BaseModel):
  category: Literal["Eligibility", "Procedure", "Documents", "Other"]
  urgency: Literal["Low", "Medium", "High"]
  requires_hr_review: bool
  summary: str


class LeaveResponse(BaseModel):
  employee_id: int
  employee_name: str
  analysis: LeaveAnalysis
  guidance: str
  next_step: str
  disclaimer: str
  status: str