from pydantic import BaseModel, Field
from typing import Literal

class CricketRequest(BaseModel):
  user_name : str = Field(min_length=2)
  knowledge_level : Literal["Beginner","Intermediate","Experienced"]
  question : str = Field(min_length=5)

class CricketResponse(BaseModel):
  user_name : str
  role : str
  answer : str