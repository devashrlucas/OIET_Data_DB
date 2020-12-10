import psycopg2
from database import db


def add_pk(t_name, c_name):
    try:
        # params = (t_name, c_name)

        # create connection and cursor using db object methods
        connection = db.connection
        cursor = db.cursor

        # call stored procedures
        cursor.execute("CALL sp_add_pk(%s, %s)", t_name, c_name)

        # commit and close using db object methods
        connection.commit
        cursor.close
    except Exception as e:
        print(e)


if __name__ == "__main__":
    add_pk("%Geo%", "%cityi%")
