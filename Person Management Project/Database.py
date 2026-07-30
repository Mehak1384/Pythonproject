import psycopg2;

connection = psycopg2.connect(
    host="localhost",
    database="PMS",
    user="postgres",
    password="411008@Pd",
    port="5432"
)

cursor = connection.cursor()
def add_person(p):
    cursor.execute(
        """
        INSERT INTO persons
        (name, dob, address, phone_number, qualification)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            p.name,
            p.DOB,
            p.Address,
            p.PhoneNumber,
            p.Qualification
        )
    )
    connection.commit()
