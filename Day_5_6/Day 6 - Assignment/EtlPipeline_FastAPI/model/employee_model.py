from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, UniqueConstraint
from config.database import Base


class Employee(Base):
  __tablename__ = "employees"

  employee_id = Column(String(10), primary_key=True)
  employee_name = Column(String(100), nullable=False)
  department = Column(String(30), nullable=False)
  city = Column(String(50))
  joining_date = Column(Date, nullable=False)


class Payroll(Base):
  __tablename__ = "payroll"
  __table_args__ = (UniqueConstraint("employee_id", "payroll_month"),)

  id = Column(Integer, primary_key=True, autoincrement=True)
  employee_id = Column(String(10), ForeignKey("employees.employee_id", ondelete="CASCADE"), nullable=False)
  payroll_month = Column(Date, nullable=False)

  basic_salary = Column(Float, nullable=False)
  hra = Column(Float, default=0)
  bonus = Column(Float, default=0)
  deductions = Column(Float, default=0)
  gross_salary = Column(Float, nullable=False)
  net_salary = Column(Float, nullable=False)

  working_days = Column(Integer, nullable=False)
  present_days = Column(Integer, nullable=False)
  attendance_pct = Column(Float)
  performance_rating = Column(Integer)
  salary_category = Column(String(20))