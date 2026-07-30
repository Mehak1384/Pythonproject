import psycopg2;

connection = psycopg2.connect(
    host="localhost",
    database="PMS",
    user="postgres",
    password="411008@Pd",
    port="5432"
)

cursor = connection.cursor()
