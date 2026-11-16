from pydantic import BaseModel

class ITSupportAnalysis(BaseModel):
  issue_category: str
  priority_level: str
  suspected_root_cause: str
  impact_level: str
  troubleshooting_steps: list[str]
  estimated_resolution_time: str | None = None