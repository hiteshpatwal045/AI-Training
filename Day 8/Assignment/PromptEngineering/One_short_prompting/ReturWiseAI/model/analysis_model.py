from typing import Literal
from pydantic import BaseModel


class ReturnAnalysis(BaseModel):
  issue_category: Literal["Damaged", "Wrong Item", "Quality", "Other"]
  urgency: Literal["Low", "Medium", "High"]
  evidence_sufficiency: Literal["Sufficient", "Insufficient", "Unclear"]
  missing_information: list[str]
  reasoning_summary: str