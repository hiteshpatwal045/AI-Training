from typing import Literal
from pydantic import BaseModel, Field


class HelpdeskRequest(BaseModel):
  employee_id: int = Field(gt=0)
  employee_name: str = Field(min_length=2)
  issue_type: str = Field(min_length=1)
  issue_description: str = Field(min_length=10)


class HelpdeskAnalysis(BaseModel):
  category: Literal["Password", "Network", "Software", "Other"]
  severity: Literal["Low", "Medium", "High"]
  needs_escalation: bool
  summary: str
  suggested_steps: list[str]
  status: str
  # escalation_message: str


class HelpdeskResponse(BaseModel):
  employee_id: int
  employee_name: str
  analysis: HelpdeskAnalysis
  suggested_steps: list[str] = Field(min_length=1)
  # escalation_message: str
  # status: str