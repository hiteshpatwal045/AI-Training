
from pydantic import BaseModel
from typing import Literal


class TrainingRequest(BaseModel):
  employee_id: int
  employee_name: str
  topic: str
  question: str


class TrainingAnalysis(BaseModel):
  category: Literal["Concept", "Coding", "Career", "Other"]
  difficulty: Literal["Beginner", "Intermediate", "Advanced"]
  priority: Literal["Low", "Medium", "High"]
  summary: str


class TrainingResponse(BaseModel):
  employee_id: int
  employee_name: str
  topic: str
  analysis: TrainingAnalysis
  answer: str
  recommended_action: str
  status: str
