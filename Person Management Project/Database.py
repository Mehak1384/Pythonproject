import psycopg2
from psycopg2 import OperationalError
def create_connection_psql():
    connection=None
    try:
        connection=psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        user="postgres",
        password="411008@Pd",
        database="PMS")
        print("Connection with postgres sql sever is done")
    except OperationalError as e:
        print(f"The error coccured is '{e}'")
        return connection
    finally:
        print("Connection is closed")
conn=create_connection_psql()
if conn:
    conn.close()
    print("Connection is closed")
        
        
