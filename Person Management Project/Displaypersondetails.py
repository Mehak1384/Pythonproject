from Database import cursor

def display():
    cursor.execute("SELECT * FROM persons")
    rows = cursor.fetchall()

    for row in rows:
        print("---------------------------")
        print("ID:", row[0])
        print("Name:", row[1])
        print("Date of Birth:", row[2])
        print("Address:", row[3])
        print("Phone Number:", row[4])
        print("Qualification:", row[5])