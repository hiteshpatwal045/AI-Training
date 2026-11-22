
from pydantic import BaseModel
from typing import Literal


class CustomerRequest(BaseModel):
  customer_id: int
  customer_name: str
  product_name: str
  query: str


class CustomerAnalysis(BaseModel):
  category: Literal["Product", "Delivery", "Return", "Payment", "Other"]
  sentiment: Literal["Positive", "Neutral", "Negative"]
  priority: Literal["Low", "Medium", "High"]
  summary: str


class CustomerResponse(BaseModel):
  customer_id: int
  customer_name: str
  analysis: CustomerAnalysis
  reply: str
  next_action: str
  status: str = "success"
