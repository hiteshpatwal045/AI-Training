from typing import Optional
from pydantic import BaseModel


class ClaimResponse(BaseModel):
  customer_name: str
  depreciation_rate: float
  depreciation_amount: float
  eligible_repair_amount: float
  covered_amount: float
  deductible: float
  claim_payout: float
  inspection_fee: float
  gst: float
  net_customer_benefit: float
  no_claim_bonus: float
  ai_explanation: Optional[str] = None


class ClaimComparisonResponse(BaseModel):
  customer_name: str
  regular: ClaimResponse
  premium: ClaimResponse
  payout_difference: float