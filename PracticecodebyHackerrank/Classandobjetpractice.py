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
s.show_details()
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
class employee:
    def __init__(self,Emp_id,name,dept,salary):
       self.employee_id=Emp_id
       self.name=name
       self.departement=dept
       self.salary=salary
    def show_details(self):
        print("Employee ID:",self.employee_id)
        print("Name:",self.name)
        print("Departement:",self.departement)
        print("Salary:",self.salary)
    def work(self):
        print("Employee is working.....")
e=employee(101,"Mehak","IT",50000)
e.show_details()
e.work()"""
"""class bank:
    def __init__(self,bank_a,a_holder,balance):
        self.acc=bank_a
        self.h=a_holder
        self.b=balance
    def show_details(self):
        print("Account Number:", self.acc)
        print("Account Holder:", self.h)
        print("Balance:", self.b)
    def deposit(self,amount):
        self.b=self.b+amount
        print("Amount deposited:",amount)
    def withdraw(self,amount):
        self.b-=amount
        print("Amount withdrawn:,",amount)
    def check_balance(self):
        print("Current Balance:",self.b)
n=bank(123,"Mehak",10000)
n.show_details()
n.deposit(5000)
n.withdraw(2000)
n.check_balance()"""
class book:
    def __init__(self,book_id,title,author,p):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.price=p
    def show_details(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
    def discount(self,dis):
        self.price=self.price-(self.price*dis/100)
    def update_price(self):
        print("Price after discount:",self.price)
b=book(101,"Python Programming","Mehak",500)
b.show_details()
b.discount(10)
b.update_price()
