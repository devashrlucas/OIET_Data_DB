import psycopg2
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


def add_fk(tb_keyword, c_name, pk_ref):
    try:
        # create connection and cursor using db object methods
        connection = db.connection
        cursor = db.cursor

        connection
        cursor

        # call stored procedure: add primary key
        cursor.execute("CALL add_foreign_key(%s, %s, %s)", (tb_keyword, c_name, pk_ref))

        # commit and close cursor using db object methods.
        connection.commit()
        cursor.close
    except Exception as e:
        print(e)


"""
add_pk(t_name="GeoIDs - City", c_name="cityid")
add_pk(t_name="GeoIDs - County", c_name="countyfips")
add_pk(t_name="GeoIDs - State", c_name="statefips")
add_pk(t_name="ACS Demographic And Housing Estimates - National - 2019", c_name="countrycode")
"""

add_fk(tb_keyword="city", c_name="cityid", pk_ref="cityid")

print("done")
