from sqlalchemy import (Column, Integer, String, Numeric)
from config.database import Base


class Employee(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    department = Column(String(100), nullable=False)
