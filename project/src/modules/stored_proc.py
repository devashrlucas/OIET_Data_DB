import psycopg2
from database import db


def add_pk(t_name, c_name):
    try:

        # create connection and cursor using db object methods
        connection = db.connection
        cursor = db.cursor
        commit = db.commit

        connection
        cursor

        # call stored procedure: add primary key
        cursor.execute("CALL add_primary_key(%s, %s)", (t_name, c_name))

        # commit and close cursor using db object methods. Do not close connection here.
        commit
        cursor.close()

    except Exception as e:
        print(e)
