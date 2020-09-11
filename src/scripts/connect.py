import psycopg2
from psycopg2 import OperationalError

try:
    connection = psycopg2.connect(
        database = "oiet_data",
        user = "oiet_admin",
        password = "admin",
        host= "127.0.0.1",
        port = "5432"
    )
    
    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE test(
        username    TEXT    NOT NULL, 
        password    CHAR(10)    NOT NULL);'''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully")
except OperationalError as e:  # Error that is typically not under programmer's control
    print(f"The error '{e}' occurred")
    


