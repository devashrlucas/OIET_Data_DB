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


def create_db():
    engine = create_engine("postgres://localhost/oiet_data")
    if not database_exists(engine.url):
        create_database(engine.url)

# Can create multiple db connections if needed
class DbConnection():
    def __init__(self): 
        self.name = os.getenv("DATABASE_NAME")
        self.login = os.getenv("DATABASE_LOGIN")
        self.password = os.getenv("DATABASE_PASSWORD")
        self.host = os.getenv("DATABASE_HOST")
        self.port = os.getenv("DATABASE_PORT")
        try:
            self.connection = psycopg2.connect(
                database=self.name,
                user=self.login,
                password=self.password,
                host=self.host,
                port=self.port
            )
        except OperationalError as oe:  # Error that is typically not under programmer's control
            print(f"The error '{oe}' occurred")
    def create_cursor(self):    
        self.cursor = self.connection.cursor()


        
