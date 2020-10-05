'''
For Mac users: please remove the '.DS_Store' file from the main directory.
If you have already done so globally, you can ignore the following set of instructions.
1) Open terminal
2) In command line, run: cd /path/to/OIET_DATA_DB
3) In command line, run: find . -name '.DS_Store' -type f -delete
'''

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv
import os


load_dotenv()


DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_LOGIN = os.getenv("DATABASE_LOGIN") 
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")

engine = create_engine("postgres://localhost/oiet_data")
if not database_exists(engine.url):
    create_database(engine.url)


try:
    connection=psycopg2.connect(
        database=DATABASE_NAME,
        user=DATABASE_LOGIN,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT
    )
    
    cursor = connection.cursor()
except OperationalError as oe:  # Error that is typically not under programmer's control
    print(f"The error '{oe}' occurred")
    


