from pydantic import BaseModel, Field
from typing import Literal


class EmpRequest(BaseModel):
    emp_id: str
    emp_name: str
    emp_rating: int = Field(ge=0, le=5)
    emp_weak_sub: str


class EmpAnalysis(BaseModel):
    emp_feedback: str
    summary: list[str]

class EmpResponse(BaseModel):
    emp_feedback: str
    summary: EmpAnalysis
