from pydantic import BaseModel
from model.analysis_model import ReturnAnalysis


class ReturnResponse(BaseModel):
  request_id: str
  analysis: ReturnAnalysis
  recommended_next_steps: list[str]
  human_review_required: bool
  customer_message_draft: str