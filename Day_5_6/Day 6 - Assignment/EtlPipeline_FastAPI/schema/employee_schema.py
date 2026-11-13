from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class EmployeeBase(BaseModel):
  employee_name: str
  department: str
  city: Optional[str] = None
  joining_date: date


class EmployeeCreate(EmployeeBase):
  employee_id: str


class EmployeeUpdate(BaseModel):
  employee_name: Optional[str] = None
  department: Optional[str] = None
  city: Optional[str] = None
  joining_date: Optional[date] = None


class EmployeeOut(EmployeeBase):
  model_config = ConfigDict(from_attributes=True)
  employee_id: str


class PayrollOut(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  id: int
  employee_id: str
  payroll_month: date
  basic_salary: float
  hra: float
  bonus: float
  deductions: float
  gross_salary: float
  net_salary: float
  working_days: int
  present_days: int
  attendance_pct: Optional[float] = None
  performance_rating: Optional[int] = None
  salary_category: Optional[str] = None


class PayrollSummary(BaseModel):
  total_gross: float
  total_net: float
  total_deductions: float
  employee_count: int
  month_count: int


class DepartmentStats(BaseModel):
  department: str
  employee_count: int
  avg_salary: float
  total_payroll: float


class TopEarner(BaseModel):
  employee_id: str
  employee_name: str
  department: str
  avg_net_salary: float


class ETLRunResponse(BaseModel):
  message: str
  employees_in_db: int
  payroll_rows_in_db: int
  details: Optional[dict] = None