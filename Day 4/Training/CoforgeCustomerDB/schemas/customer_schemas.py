from decimal import Decimal
from pydantic import BaseModel, Field, EmailStr, ConfigDict


class EmployeeBase(BaseModel):
    customer_name: str = Field(min_length=2)
    age: int = Field(ge=18, le=70)
    email: EmailStr
    department: str = Field(min_length=2)


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    customer_id: int
    model_config = ConfigDict(from_attributes=True)


class DepartmentCount(BaseModel):
    department: str
    employee_count: int
