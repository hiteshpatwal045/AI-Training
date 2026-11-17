from pydantic import BaseModel, Field
from typing import Dict, Literal


class HospitalAskResponse(BaseModel):
    status: Literal["success", "error", "needs_clarification"]
    response: str
    tools_used: list[str]
    data: Dict
