import psycopg2
from psycopg2 import sql
from database import db


def add_pk(t_name, c_name):
    try:

        # create connection and cursor using db object methods
        connection = db.connection
        cursor = db.cursor

        connection
        cursor

        # call stored procedure: add primary key
        cursor.execute("CALL add_primary_key(%s, %s)", (t_name, c_name))

        # commit and close cursor using db object methods.
        connection.commit()
        cursor.close

    except Exception as e:
        print(e)


add_pk(t_name="GeoIDs - City", c_name="cityid")
add_pk(t_name="GeoIDs - State", c_name="statefips")
print("done")
