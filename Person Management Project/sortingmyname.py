from Persondetails import person
from Displaypersondetails import display 
def sort(persons):

    count = len(persons)

    print("Based on Data there are 3 type of sorting required for this program")
    print("1. Sort by Person Name")
    print("2. Sort by Date of Birth")
    print("3. Sort by Qualification")

    ch = int(input("Please provide your choice for sorting: "))

    match ch:

        case 1:
            print("Sorting by Name")

            for i in range(0, count):
                for j in range(i + 1, count):

                    if persons[i].name > persons[j].name:
                        temp = persons[i]
                        persons[i] = persons[j]
                        persons[j] = temp

            for i in range(0, count):
                print("--------------------------------")
                print("Name:", persons[i].name)
                print("DOB:", persons[i].DOB)
                print("Address:", persons[i].Address)
                print("Phone Number:", persons[i].PhoneNumber)
                print("Qualification:", persons[i].Qualification)

        case 2:
            print("Sorting by Date of Birth")

            for i in range(0, count):
                for j in range(i + 1, count):

                    if persons[i].DOB > persons[j].DOB:
                        temp = persons[i]
                        persons[i] = persons[j]
                        persons[j] = temp

            for i in range(0, count):
                print("--------------------------------")
                print("Name:", persons[i].name)
                print("DOB:", persons[i].DOB)
                print("Address:", persons[i].Address)
                print("Phone Number:", persons[i].PhoneNumber)
                print("Qualification:", persons[i].Qualification)

        case 3:
            print("Sorting by Qualification")

            for i in range(0, count):
                for j in range(i + 1, count):

                    if persons[i].Qualification > persons[j].Qualification:
                        temp = persons[i]
                        persons[i] = persons[j]
                        persons[j] = temp

            for i in range(0, count):
                print("--------------------------------")
                print("Name:", persons[i].name)
                print("DOB:", persons[i].DOB)
                print("Address:", persons[i].Address)
                print("Phone Number:", persons[i].PhoneNumber)
                print("Qualification:", persons[i].Qualification)

        case 4:
            print("Invalid Choice")