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
PATH_TO_DATA = os.getenv("PATH_TO_DATA")


city_keyword = "City"
county_keyword = "County"
state_keyword = "State"
national_keyword = "National"


connection = psycopg2.connect(
    database=DATABASE_NAME,
    user=DATABASE_LOGIN,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT,
)

cursor = connection.cursor()

try:
    SQL = "SELECT * FROM information_schema.tables WHERE table_schema = (%s);"
    data = ("public",)
    cursor.execute(SQL, data)
    connection.commit()
    print("query executed successfully")
except OperationalError as e:  # Error that is typically not under programmer's control
    print(f"The error '{e}' occurred")


"""
if data_file == f'ACS Demographic And Housing Estimates - National - 2019.csv':
    column = "countrycode"
    parent = 'ACS Demographic And Housing Estimates - National - 2019.csv'
    query = f'ALTER TABLE "{sorted(data_directory)[i]}" ADD CONSTRAINT country FOREIGN KEY ({column}) REFERENCES parent ({column}) MATCH FULL'
    cursor.execute(query)
    connection.commit()
    connection.close()
"""
