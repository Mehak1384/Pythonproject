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
        while True:
            person_name=input("Enter the name of person:")
            person_email=input("Enter the email of person:")
            person_phone=input("Enter the phone number of person:")
            person_address=input("Enter the address of person:")
            person_dob=input("Enter the date of birth of person in YYYY-MM-DD format:")
            person_male=bool(input("Enter the gender of person(False for male / True for female):"))
            person_education=input("Enter the education of person:")
            query_table="""insert into person_management_system(
            person_name,
            person_email,
            person_phone,
            person_address,
            person_dob,
            person_male,
            person_education)
            VALUES (%s, %s, %s, %s, %s, %s, %s);"""
            values = (
                        person_name,
                        person_email,
                        person_phone,
                        person_address,
                        person_dob,
                        person_male,
                        person_education
                    )
            print(type(values))
            cursor.execute(query_table,values)
            connection.commit()
            choice=input("Do you want to add more details in database:(yes/no):")
            if choice=="No" or choice=="no":
                break
        print("Table created successfully in PostgreSQL")
        return connection
    except OperationalError as e:
        print(f"The error coccured is '{e}'")
        return connection
    finally:
        print("Connection")
conn=create_connection_psql()
if conn:
    curs=conn.cursor()
    query_select="""select * from person_management_system;"""
    curs.execute(query_select)
    rows=curs.fetchall()
    for i  in rows:
        print(i)
    print("Sorted Elements By their Name:")
    query_sort="""select*from person_management_system order by person_name asc ;"""
    curs.execute(query_sort)
    r_ows=curs.fetchall()
    for j in r_ows:
        print(j)
    print("Sorted Elements By their Gender and Date of Birth:")
    query_sort="""select*from person_management_system order by person_male asc,person_dob asc;"""
    curs.execute(query_sort)
    r_ows=curs.fetchall()
    for j in r_ows:
            print(j)
    conn.close()
    


        
        
