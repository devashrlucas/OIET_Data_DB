"""
Attributions:
* Database class definition in Python: [Stack Overflow](https://stackoverflow.com/a/38078544/) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.
"""

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


class Database:
    def __init__(self, name):
        self.name = os.getenv("DATABASE_NAME")
        self.login = os.getenv("DATABASE_LOGIN")
        self.password = os.getenv("DATABASE_PASSWORD")
        self.host = os.getenv("DATABASE_HOST")
        self.port = os.getenv("DATABASE_PORT")
        self.url = os.getenv("URL")
        try:
            self.connection = psycopg2.connect(
                database=self.name,
                user=self.login,
                password=self.password,
                host=self.host,
                port=self.port,
            )
        except OperationalError as oe:
            print(f"The error '{oe}' occurred")

    # makes and returns db connection in with statements
    def __enter__(self):
        return self

    # closes db connection in with statements
    def __exit__(self, exeception_type, exception_value, exception_traceback):
        self.close()

    # getter
    @property
    def cursor(self):
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def add_primary_key(self, table_name, column_name):
        sql = "ALTER TABLE {table_name} ADD PRIMARY KEY {column_name}".format(
            table_name, column_name
        )
        return self.query(sql)

    def add_foreign_key(
        self, table_name, column_name, fk_column, parent_table, parent_key_column
    ):
        sql = "ALTER TABLE {table_name} CONSTRAINT FOREIGN KEY {fk_column} REFERENCES {parent_table}({parent_key_column})".format(
            table_name, column_name, fk_column, parent_table, parent_key_column
        )
        return self.query(sql)
