from Persondetails import person
from Displaypersondetails import display
from sortingmyname import sort
from Database import add_person
while True:
    p = person()
    add_person(p)
    choice = input("Do you want to enter another person (Y/N): ")
    if choice=="N" or choice=="n":
        break
print("Total number of persons entered:", count)
display()
