import os
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

URL_OBJ = URL.create(
  drivername="mysql+pymysql",
  username  =os.getenv("db_username"),
  password  =os.getenv("db_password"),
  host      =os.getenv("db_host"),
  port      =int(os.getenv("db_port",3306)),
  database  =os.getenv("db_database")
)

engine = create_engine(URL_OBJ)
SessionLocal = sessionmaker(bind=engine,autoflush=True,autocommit=False)
Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

