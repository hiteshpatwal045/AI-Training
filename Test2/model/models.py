from pydantic import BaseModel, Field


class EmpRequest(BaseModel):
    employee_id: str = Field(min_length=1)
    employee_name: str
    leave_type: str
    number_of_days: int = Field(ge=1, le=30)
    reason: str = Field(min_length=10)


class EmpResponse(BaseModel):
    employee_id: str
    summary: str
    recommendation_action: str
    status: str
