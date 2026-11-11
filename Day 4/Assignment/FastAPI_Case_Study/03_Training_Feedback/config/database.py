import os
from dotenv import load_dotenv
from sqlalchemy.engine import create_engine
from sqlalchemy import URL
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DB_OBJ = URL.create(
  drivername="mysql+pymysql",
  username  =os.getenv("db_username"),
  password  =os.getenv("db_password"),
  host      =os.getenv("db_host"),
  port      =int(os.getenv("db_port",3306)),
  database  =os.getenv("db_database")
)


engine = create_engine(DB_OBJ)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()