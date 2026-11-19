from pydantic import BaseModel, Field
from typing import Literal


class OrderItem(BaseModel):
  food_name: str
  quantity: int = Field(gt=0)


class OrderRequest(BaseModel):
  employee_id: str
  employee_name: str
  items: list[OrderItem] = Field(min_length=1)


class InvoiceResponse(BaseModel):
  invoice_id: str
  order_id: str
  employee_id: str
  employee_name: str
  status: str
  line_items: list[dict]
  subtotal: float
  gst: float
  total_payable: float


class OrderResponse(BaseModel):
  order_id: str
  employee_id: str
  employee_name: str
  status: str

  elapsed_minutes: int | None = None
  expected_minutes: int | None = None
  delay_minutes: int | None = None
  priority: Literal["NORMAL", "HIGH", "CRITICAL"] | None = None
  escalated_to: str | None = None
  message: str | None = None

class EscalationResponse(BaseModel):
  priority: Literal["HIGH", "CRITICAL"]
  recipient: str
  message: str