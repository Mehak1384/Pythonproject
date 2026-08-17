"""Create a Student class with name, age, and marks. Add a method display_result()
that prints the student's details and whether the student has passed or failed.

Create 3 student objects and test them."""
class student:
    def __init__(self,name,age,marks):
        self.n=name
        self.a=age
        self.m=marks
    def display_result(self):
        print("Student Name:",self.n)
        print("Student Age:",self.a)
        if(self.m>=33):
            print("Student is pass")
        else:
            print("Student is fail")
detail=student("Mehak",22,100)
detail.display_result()
details_2=student("Bhavya",17,90)
details_2.display_result()
details3=student("Ash",7,28)
details3.display_result()