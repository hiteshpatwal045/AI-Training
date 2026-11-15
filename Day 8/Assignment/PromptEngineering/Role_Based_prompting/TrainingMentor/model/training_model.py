from pydantic import BaseModel, Field
from typing import Literal

class TrainingRequest(BaseModel):
  emp_name : str
  exp_level : Literal["Beginner","Intermediate","Experienced"]
  question : str

class TrainingResponse(BaseModel):
  emp_name : str
  role : str
  answer : str
