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
        print(type(connection))
        cursor=connection.cursor()
        query="""create table if not exists person_management_system(
                person_id serial primary key,
                person_name varchar(50) not null,
                person_email varchar(50) not null,
                person_phone varchar(50) not null,
                person_address varchar(100) not null,
                person_dob date not null,
                person_male boolean not null,
                person_education varchar(50) not null);"""
        cursor.execute(query)
        connection.commit()

        print("Table created successfully in PostgreSQL")
    except OperationalError as e:
        print(f"The error coccured is '{e}'")
        return connection
    finally:
        print("Connection is closed")
conn=create_connection_psql()
if conn:
    conn.close()
    print("Connection is closed")

        
        
