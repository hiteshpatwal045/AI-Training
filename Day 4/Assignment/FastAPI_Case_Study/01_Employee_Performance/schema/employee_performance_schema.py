from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal

class CreateEmployeePerformance(BaseModel):
  emp_name : str
  emp_department : str
  emp_designation : str
  emp_salary : Decimal = Field(gt = 0)
  emp_performance_rating : float = Field(ge=1, le=5)
  emp_project_completed : int = Field(ge=0)
  emp_attendance_percentage : float = Field(ge=0, le=100)
  emp_review_year :int

class UpdateEmployeePerformance(BaseModel):
  emp_performance_rating : float | None = Field(default=None,ge=1, le=5)
  emp_attendance_percentage : float | None = Field(default=None,ge=0, le=100)
  emp_project_completed : int | None = Field(default=None,ge=0)

class DepartmentAverageResponse(BaseModel):
  emp_department : str
  emp_performance_rating : float
  model_config = ConfigDict(from_attributes=True)

class EmployeeClassificationResponse(BaseModel):
  emp_id : int
  emp_name : str
  emp_rating : float
  category : str

class ResponseEmployeePerformance(CreateEmployeePerformance):
  emp_id: int
  model_config = ConfigDict(from_attributes=True)
