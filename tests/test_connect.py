# This testing method is based off the solution written by Minul Lamahewage: 
# "Python Testing With a Mock Database"
# https://medium.com/swlh/python-testing-with-a-mock-database-sql-68f676562461

from unittest import TestCase
from unittest.mock import patch

import psycopg2
from psycopg2 import OperationalError


from dotenv import load_dotenv
import os
import sys

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_LOGIN = os.getenv("DATABASE_LOGIN")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")


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
    #drop db if already exists
    

