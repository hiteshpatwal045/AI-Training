import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.engine import URL

load_dotenv()


class Base(DeclarativeBase):
    pass

# username = os.getenv("DB_USERNAME")
# password = os.getenv("DB_PASSWORD")
# database = os.getenv("DB_DATABASE")

# print("Username:", username)
# print("Password:", password)
# print("Database:", database)


database_url = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_DATABASE")
)

engine = create_engine(
    database_url
)

sessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
