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


#  db object with 1 connection and 1 cursor. Limit number of connections. Multiple cursors ok.
class Database:
    def __init__(self):
        self.name = os.getenv("DATABASE_NAME")
        self.login = os.getenv("DATABASE_LOGIN")
        self.password = os.getenv("DATABASE_PASSWORD")
        self.host = os.getenv("DATABASE_HOST")
        self.port = os.getenv("DATABASE_PORT")
        self.url = os.getenv("URL")
        try:
            self._connection = psycopg2.connect(
                database=self.name,
                user=self.login,
                password=self.password,
                host=self.host,
                port=self.port,
            )
        except OperationalError as oe:
            print(f"The error '{oe}' occurred")
        self._cursor = self._connection.cursor()

    # Makes and returns db connection in with statements
    def __enter__(self):
        return self

    # Closes db connection in with statements
    def __exit__(self, exeception_type, exception_value, exception_traceback):
        self.close()

    # getter
    @property
    def connection(self):
        return self._connection

    # getter
    @property
    def cursor(self):
        return self._cursor

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

    # creates stored procedure for add primary key in database
    def sp_add_pk(self, t_name, c_name):
        connection = self.connection
        cursor = self.cursor
        commit = self.commit

        sql = "CREATE OR REPLACE PROCEDURE public.add_primary_key(IN t_name character varying, IN c_name character varying) LANGUAGE 'plpgsql' AS $$ BEGIN  'ALTER TABLE ' || quote_ident(t_name) || ' ADD PRIMARY KEY ' || '(' || quote_ident(c_name) || ')'; END; $$;"
        cursor.execute(sql)

    def sp_add_fk(self, tb_keyword, c_name, p_table, pk_ref):
        connection = self.connection
        cursor = self.cursor
        commit = self.commit
        sql = "CREATE OR REPLACE PROCEDURE public.add_foreign_key(IN tb_keyword character varying, IN c_name character varying, IN p_table varchar, IN pk_ref character varying) LANGUAGE 'plpgsql' AS $$ DECLARE row record; t_name varchar; BEGIN FOR row IN (SELECT table_schema, table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema='public' AND table_name NOT LIKE '%Geo' AND table_name NOT LIKE '%ACS' AND table_name LIKE tb_keyword) LOOP EXECUTE 'ALTER TABLE ' || quote_ident(row.table_name) || ' ADD CONSTRAINT ADD FOREIGN KEY ' || '(' || quote_ident(c_name) || ')' || 'REFERENCES ' || quote_ident(p_table) || ' (' || quote_ident(pk_ref) || ')'; END LOOP; END; $$;"

        # sql = "CREATE OR REPLACE PROCEDURE public.add_foreign_key(IN tb_keyword character varying, IN c_name character varying, IN pk_ref character varying) LANGUAGE 'plpgsql' AS $$ BEGIN 'ALTER TABLE ' || quote_ident(tb_name) || ' ADD CONSTRAINT ADD FOREIGN KEY ' || '(' || quote_ident(c_name) || ')' || 'REFERENCES parent_table ' || '(' || quote_ident(pk_ref) || ')'; END; $$;"
        cursor.execute(sql)
        connection.commit()


# for import into other modules
db = Database()
"""
db.sp_add_fk(
    tb_keyword="city", c_name="cityid", p_table="GeoIDs - City", pk_ref="cityid"
)
db.sp_add_fk(
    tb_keyword="state", c_name="statefips", p_table="GeoIDs - State", pk_ref="statefips"
)
"""
print("db.py done")
