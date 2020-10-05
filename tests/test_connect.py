# This testing method is based off the solution written by Minul Lamahewage: 
# "Python Testing With a Mock Database"
# https://medium.com/swlh/python-testing-with-a-mock-database-sql-68f676562461

# PLEASE NOTE: database server must be running prior to test

from unittest import TestCase
from unittest.mock import patch

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


# Superclass for several test cases using same test database 
class MockDB(TestCase):
    @classmethod
    def setUpClass(cls):
        connection = psycopg2.connect(
            database=DATABASE_NAME,
            user=DATABASE_LOGIN,
            password=DATABASE_PASSWORD,
            host=DATABASE_HOST,
            port=DATABASE_PORT
        )
        cursor = connection.cursor()
# Drop database if already exists
        try:
            cursor.execute("DROP DATABASE IF EXISTS test")
            cursor.close()
            print("Database dropped")
        except OperationalError as oe:  # Error that is typically not under programmer's control
            print(f"The error '{oe}' occurred")
        try:
# Create test table
            create_table_query = '''CREATE TABLE test(
                username    TEXT    NOT NULL, 
                password    CHAR(10)    NOT NULL);'''
            cursor.execute(create_table_query)
            connection.commit()
            print("Table created successfully")
        except OperationalError as oe:  # Error that is typically not under programmer's control
            print(f"The error '{oe}' occurred")
