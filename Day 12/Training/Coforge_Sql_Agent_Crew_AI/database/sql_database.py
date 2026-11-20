import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()


def get_connection():
    result = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        connection_timeout=10
    )
    return result
