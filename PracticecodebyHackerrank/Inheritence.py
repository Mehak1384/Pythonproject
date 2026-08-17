"""Create the following hierarchy:
Person
   ↓
Employee
   ↓
Manager
Person → name, age
Employee → employee_id, salary
Manager → department
Create a Manager object and display all information."""
class Person:
    def __init__(self,name,age):
        self.n=name
        self.a=age
class Employee(Person):
    def __init__(self,employee_id,salary,name,age):
        super().__init__(name,age)
        self.e=employee_id
        self.s=salary
class Manager(Employee):
     def __init__(self,name,age,employee_id,salary,department):
         super().__init__(employee_id,salary,name,age)
         self.d=department
     def display(self):
        print("Name:", self.n)
        print("Age:", self.a)
        print("Employee ID:", self.e)
        print("Salary:", self.s)
        print("Department:", self.d)
m = Manager("Mehak", 22, 7138, 50000, "IT")
m.display()

             