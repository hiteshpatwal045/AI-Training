import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

URL_OBJ = URL.create(
  drivername= "mysql+pymysql",
  username  = os.getenv("db_username"),
  password  = os.getenv("db_password"),
  host      = os.getenv("db_host"),
  port      = int(os.getenv("db_port",3306)),
  database  = os.getenv("db_database")
)

#step1. build the connection to your database:
engine  = create_engine(URL_OBJ)
#step2. creates a factory that makes database sessions.
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)
#step3. creates the parent class for your tables
Base = declarative_base()

def get_db():
  try:
    db = SessionLocal()
    yield db
  finally:
    db.close()