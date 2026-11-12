from datetime import date
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field

AccountType = Literal["Savings", "Current"]

class OpenAccount(BaseModel):
  customer_name  : str = Field(min_length=1, max_length=100)
  email          : EmailStr
  account_number : str = Field(min_length=1, max_length=20)
  account_type   : AccountType
  branch_name    : str = Field(min_length=1, max_length=100)
  balance        : Decimal = Field(default=Decimal("0"), ge=0, max_digits=15, decimal_places=2)
  opened_on      : date


class BankCustomer(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  customer_id    : int
  customer_name  : str
  email          : EmailStr
  account_number : str
  account_type   : AccountType
  branch_name    : str
  balance        : Decimal
  is_active      : bool
  opened_on      : date


class CustomerPage(BaseModel):
  items     : list[BankCustomer]
  total     : int
  page      : int
  page_size : int

class UpdateCustomer(BaseModel):
  customer_name : str | None = Field(default=None, min_length=1, max_length=100)
  email         : EmailStr | None = None
  branch_name   : str | None = Field(default=None, min_length=1, max_length=100)


class Deposit(BaseModel):
  amount : Decimal = Field(gt=0, max_digits=15, decimal_places=2)

class Withdraw(BaseModel):
  amount : Decimal = Field(gt=0, max_digits=15, decimal_places=2)


class BranchDeposit(BaseModel):
  branch_name    : str
  total_deposits : Decimal