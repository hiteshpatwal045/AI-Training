from pydantic import BaseModel
from model.analysis_model import ITSupportAnalysis

class ITSupportResponse(BaseModel):
  ticket_id: str
  ticket_status: str
  analysis: ITSupportAnalysis
  recommended_actions: list[str]
  escalation_required: bool
  ai_summary: str