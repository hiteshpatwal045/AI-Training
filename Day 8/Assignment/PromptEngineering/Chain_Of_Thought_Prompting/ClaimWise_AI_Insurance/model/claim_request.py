from typing import Literal
from pydantic import BaseModel, Field


class ClaimRequest(BaseModel):
  customer_name: str = Field(min_length=2)
  customer_category: Literal["Regular", "Premium"]
  policy_number: str = Field(min_length=1)
  vehicle_age_years: int = Field(ge=0, le=50)
  claimed_repair_cost: float = Field(ge=5000, le=1000000)
  coverage_limit: float = Field(gt=0)
  next_renewal_base_premium: float = Field(gt=0)
  claim_filed: bool