from typing import Literal
from pydantic import BaseModel, Field


class IncidentRequest(BaseModel):
  employee_id: str = Field(min_length=1)
  employee_name: str = Field(min_length=2)
  department: str = Field(min_length=2)
  issue: str = Field(min_length=10)


class IncidentAnalysis(BaseModel):
  category: Literal["Network", "Application", "Password", "Server", "Database", "Other"]
  priority: Literal["Critical", "High", "Medium", "Low"]
  summary: str
  business_impact: str
  suggested_resolution: str


class IncidentResponse(BaseModel):
  employee_id: str
  employee_name: str
  category: str
  priority: str
  summary: str
  suggested_resolution: str
  escalation_required: bool
  status: str