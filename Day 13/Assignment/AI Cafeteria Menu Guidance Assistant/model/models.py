from typing import Literal
from pydantic import BaseModel, Field


class CafeteriaRequest(BaseModel):
  employee_id: int = Field(gt=0)
  employee_name: str = Field(min_length=2)
  food_preference: Literal["Vegetarian", "Non-Vegetarian"]
  budget: float = Field(gt=0)
  question: str = Field(min_length=10)


class CafeteriaAnalysis(BaseModel):
  meal_type: Literal["Breakfast", "Lunch", "Snack", "Dinner"]
  budget_category: Literal["Economy", "Standard", "Premium"]
  preference_match: bool
  summary: str
  suggested_meal: str
  estimated_price: float
  reason: str


class CafeteriaResponse(BaseModel):
  employee_id: int
  employee_name: str
  analysis: CafeteriaAnalysis
  suggested_meal: str
  estimated_price: float = Field(ge=0)
  reason: str
  status: str