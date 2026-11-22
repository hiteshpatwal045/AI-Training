from pydantic import BaseModel, Field


class ReturnRequest(BaseModel):
  request_id: str = Field(min_length=1)
  order_id: str = Field(min_length=1)
  product_category: str = Field(min_length=1)
  days_since_delivery: int = Field(ge=0)
  item_price_inr: float = Field(gt=0)
  reason: str = Field(min_length=1)
  item_condition: str = Field(min_length=1)
  evidence_provided: list[str]
  customer_description: str = Field(min_length=1)