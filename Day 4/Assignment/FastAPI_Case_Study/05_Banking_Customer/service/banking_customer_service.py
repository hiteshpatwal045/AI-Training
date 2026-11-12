from decimal import Decimal
from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from logger import logger
from model.banking_customer_model import BankingCustomerDB as Customer
from schema.banking_customer_schema import AccountType, OpenAccount, UpdateCustomer


# create account
def open_account(db: Session, data: OpenAccount):
  account = Customer(**data.model_dump())
  db.add(account)
  try:
    db.commit()
  except IntegrityError:
    db.rollback()
    logger.warning("Duplicate account number or email")
    raise HTTPException(
      status_code=409,
      detail="Account number or email already exists"
    )
  db.refresh(account)
  logger.info(f"Account opened: {account.customer_id}")
  return account


# fetch all the account
def list_accounts(db: Session):
  return db.query(Customer).all()


# fetch account by id
def get_account_by_number(db: Session, account_number: str):
  account = db.query(Customer).filter(Customer.account_number == account_number).first()
  if not account:
    logger.warning("Account not found")
    raise HTTPException(
      status_code=404,
      detail="Account not found"
    )
  return account

# update account
def update_account(db: Session, account_number: str, data: UpdateCustomer):
  account = db.query(Customer).filter(Customer.account_number == account_number).first()
  if not account:
    logger.warning("Account not found")
    raise HTTPException(
      status_code=404,
      detail="Account not found"
    )
  for field, value in data.model_dump(exclude_unset=True).items():
    setattr(account, field, value)
  db.commit()
  db.refresh(account)
  logger.info(f"Account updated: {account.customer_id}")
  return account

# close account
def close_account(db: Session, account_number: str):
  account = db.query(Customer).filter(Customer.account_number == account_number).first()
  if not account:
    logger.warning("Account not found")
    raise HTTPException(
      status_code=404,
      detail="Account not found"
    )
  if account.balance != 0:
    logger.warning("Close failed: balance not zero")
    raise HTTPException(
      status_code=409,
      detail="Balance must be zero to close the account"
    )
  account.is_active = False
  db.commit()
  logger.info(f"Account closed: {account.customer_id}")
  return {
    "detail": "Account closed"
  }

# 6. Filter accounts by branch
def get_accounts_by_branch(db: Session, branch_name: str):
  return db.query(Customer).filter(Customer.branch_name == branch_name).all()


# 7. Filter accounts by account type
def get_accounts_by_type(db: Session, account_type: AccountType):
  return db.query(Customer).filter(Customer.account_type == account_type).all()

# 8. Deposit into an active account
def deposit_amount(db: Session, account_number: str, amount: Decimal):
  account = db.query(Customer).filter(Customer.account_number == account_number).first()
  if not account:
    logger.warning("Account not found")
    raise HTTPException(
      status_code=404,
      detail="Account not found"
    )
  if not account.is_active:
    logger.warning("Deposit on inactive account")
    raise HTTPException(
      status_code=409,
      detail="Account is inactive"
    )
  account.balance += amount
  db.commit()
  db.refresh(account)
  logger.info(f"Deposit done: {account.customer_id}")
  return account


# 9. Withdraw from an active account (no overdraft)
def withdraw_amount(db: Session, account_number: str, amount: Decimal):
  account = db.query(Customer).filter(Customer.account_number == account_number).first()
  if not account:
    logger.warning("Account not found")
    raise HTTPException(
      status_code=404,
      detail="Account not found"
    )
  if not account.is_active:
    logger.warning("Withdraw on inactive account")
    raise HTTPException(
      status_code=409,
      detail="Account is inactive"
    )
  if account.balance < amount:
    logger.warning("Insufficient funds")
    raise HTTPException(
      status_code=409,
      detail="Insufficient funds"
    )

  account.balance -= amount

  db.commit()
  db.refresh(account)
  logger.info(f"Withdrawal done: {account.customer_id}")
  return account


# 10. Total deposits held by each branch