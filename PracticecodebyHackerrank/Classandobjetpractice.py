"""class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def show_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)
Name=input("Enter Name:")
age=int(input("Enter Age:"))
course=input("Enter course:")
s=student(Name,age,course)
s.show_details()"""
class car:
    def __init__(self,b,m,c,p):
        self.brand=b
        self.model=m
        self.color=c
        self.price=p
    def show_details(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Color:",self.color)
        print("Price:",self.price)
    def start(self):
        print("Car is starting.....")
    def stop(self):
        print("Car is stopping.....")
c=car("Toyota","Fortuner","Black",4500000)
c.show_details()
c.start()
c.stop()