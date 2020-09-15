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


try:
    connection=psycopg2.connect(
        database=DATABASE_NAME,
        user=DATABASE_LOGIN,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT
    )
    
    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE test(
        username    TEXT    NOT NULL, 
        password    CHAR(10)    NOT NULL);'''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully")
except OperationalError as e:  # Error that is typically not under programmer's control
    print(f"The error '{e}' occurred")
    


