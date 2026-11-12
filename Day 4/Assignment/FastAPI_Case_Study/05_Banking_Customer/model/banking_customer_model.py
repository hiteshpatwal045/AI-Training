from sqlalchemy import Column, Integer, String, Boolean, Numeric, Date
from config.database import Base


class BankingCustomerDB(Base):
  __tablename__ = "bankingcustomertable"

  customer_id    = Column(Integer, primary_key=True, autoincrement=True)
  customer_name  = Column(String(100), nullable=False)
  email          = Column(String(255), unique=True, nullable=False)
  account_number = Column(String(20), unique=True, nullable=False)
  account_type   = Column(String(10), nullable=False)
  branch_name    = Column(String(100), nullable=False)
  balance        = Column(Numeric(15, 2), nullable=False, default=0)
  is_active      = Column(Boolean, nullable=False, default=True)
  opened_on      = Column(Date, nullable=False)