from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from config.database import Base, engine, get_db
from schema.banking_customer_schema import (
  AccountType, BankCustomer,
  Deposit, OpenAccount, UpdateCustomer, Withdraw,
)

import service.banking_customer_service as service

Base.metadata.create_all(bind=engine)
app = FastAPI()


# 1. Open a customer account
@app.post("/customers", response_model=BankCustomer, status_code=201)
def open_account(data: OpenAccount, db: Session = Depends(get_db)):
  return service.open_account(db, data)


# 2. List all accounts
@app.get("/customers", response_model=list[BankCustomer])
def list_accounts(db: Session = Depends(get_db)):
  return service.list_accounts(db)



# 10. Total deposits per branch (must be above /customers/{account_number})


# 6. Filter by branch
@app.get("/customers/by-branch/{branch_name}", response_model=list[BankCustomer])
def get_accounts_by_branch(branch_name: str, db: Session= Depends(get_db)):
  return service.get_accounts_by_branch(db, branch_name)


# 7. Filter by account type
@app.get("/customers/by-type/{account_type}", response_model=list[BankCustomer])
def get_accounts_by_type(account_type: AccountType, db: Session= Depends(get_db)):
  return service.get_accounts_by_type(db, account_type)


# 3. Get an account by account number
@app.get("/customers/{account_number}", response_model=BankCustomer)
def get_account_by_number(account_number: str, db: Session = Depends(get_db)):
  return service.get_account_by_number(db, account_number)


# 4. Update contact or branch details
@app.put("/customers/{account_number}", response_model=BankCustomer)
def update_account(account_number: str,data: UpdateCustomer,db: Session= Depends(get_db)):
  return service.update_account(db, account_number, data)


# 5. Close an account (only if balance is zero)
@app.delete("/customers/{account_number}")
def close_account(account_number: str, db: Session = Depends(get_db)):
  return service.close_account(db, account_number)


# 8. Deposit
@app.post("/customers/{account_number}/deposit", response_model=BankCustomer)
def deposit_amount(account_number: str,data: Deposit,db: Session= Depends(get_db)):
  return service.deposit_amount(db, account_number, data.amount)


# 9. Withdraw
@app.post("/customers/{account_number}/withdraw", response_model=BankCustomer)
def withdraw_amount(account_number: str,data: Withdraw,db: Session= Depends(get_db)):
  return service.withdraw_amount(db, account_number, data.amount)