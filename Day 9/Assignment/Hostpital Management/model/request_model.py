from pydantic import BaseModel, Field
from typing import Literal


class HospitalAskRequest(BaseModel):
    message: str
    user_role: Literal["receptionist", "doctor","nurse", "billing_staff", "guest"]
