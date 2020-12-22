import psycopg2
from database import db


def add_pk(t_name, c_name):
    try:

        # create connection and cursor using db object methods
        connection = db.connection
        cursor = db.cursor
        commit = db.commit
        close = db.close

        # call stored procedure: add primary key
        db.sp_add_pk(t_name, c_name)

        # commit and close using db object methods
        cursor.close()
        commit
        close

    except Exception as e:
        print(e)
