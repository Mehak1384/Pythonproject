from empolyeedetails import details
from empdisplay import emdisplay
print("Welcome to Employee Registration System")
count=0
while True:
    Empname,Empage,Empposition,Empcode,Empexperince,Empqulation=details()
    count=+1
    choice=input("Enter you want to enter the more Emp")
    if choice== "N" or choice=="n":
        break
emdisplay(Empname,Empage,Empposition,Empcode,Empexperince,Empqulation)
