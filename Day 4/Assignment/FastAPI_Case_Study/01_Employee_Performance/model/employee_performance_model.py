from sqlalchemy import Column, Integer, String, Float
from config.database import Base

class EmployeePerformance(Base):
  __tablename__ = "employee_performance"

  emp_id = Column(Integer,primary_key=True,autoincrement=True)
  emp_name = Column(String(100),nullable=False)
  emp_department = Column(String(100),nullable=False)
  emp_designation = Column(String(100),nullable=False)
  emp_salary = Column(Float,nullable=False)
  emp_performance_rating = Column(Float,nullable=False)
  emp_project_completed = Column(Integer,nullable=False)
  emp_attendance_percentage = Column(Float,nullable=False)
  emp_review_year = Column(Integer,nullable=False)