from Persondetails import person
from Displaypersondetails import display
from sortingmyname import sort

persons = []
while True:

    p = person()
    persons.append(p)
    choice = input("Do you want to enter another person (Y/N): ")
    if choice=="N" or choice=="n":
        break
print("Total number of persons entered:", len(persons))
sort(persons)
display(persons)
