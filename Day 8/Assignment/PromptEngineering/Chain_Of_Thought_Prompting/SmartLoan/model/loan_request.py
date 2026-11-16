from pydantic import BaseModel, Field

class LoanRequest(BaseModel):
  customer_name: str
  customer_category: str
  loan_type: str
  loan_amount: float = Field(ge=50000, le=5000000)
  annual_interest_rate: float = Field(ge=7, le=18)
  loan_tenure_years: int = Field(ge=1, le=30)
