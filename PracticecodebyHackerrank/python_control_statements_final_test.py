"""Write a Python program that takes marks of 3 subjects from the user.
Calculate:
Total
Percentage
Then assign a grade:
Percentage ≥ 80 → A
Percentage ≥ 60 → B
Percentage ≥ 40 → C
Percentage < 40 → Fail
Also check whether the student has passed all three subjects individually.
A student passes a subject if marks ≥ 40.
Example:
Enter marks of subject 1: 75
Enter marks of subject 2: 65
Enter marks of subject 3: 80
Total = 220
Percentage = 73.33
Grade = B
Result = Pass
Concepts: if-elif-else, nested conditions, arithmetic."""
sub1=int(input("Enter the marks of Physics out of 100:"))
sub2=int(input("Enter the marks of chemistry out of 100:"))
sub3=int(input("Enter the marks of maths out of 100:"))
if(sub1>=40 and sub2>=40 and sub3>=40):
    print("Student is pass in all subjects")
elif(sub1<40 and sub2>=40 and sub3>=40):
    print("Student is fail in Physics and pass in CM ")
elif(sub1>=40 and sub2<40 and sub3>=40):
    print("Student is fail in Chemsitry and pass in PM ")
elif(sub1>=40 and sub2>=40 and sub3<40):
    print("Student is fail in Mathematics and pass in CP ")
else:
    print("Student is fail in two or three subjects")
t=sub1+sub2+sub3
per=t/3
display="""Percentage ≥ 80 → A
Percentage ≥ 60 → B
Percentage ≥ 40 → C
Percentage < 40 → Fail"""
if (per>=80):
    result="Pass"
    print("A",result)
elif(per>=60):
    result="Pass"
    print("B",result)
elif(per>=40):
    result="Pass"
    print("C",result)
else:
    print("Fail")
"""Question 2 — Number Table with Conditions
Take a positive integer n from the user.
Use a for loop from 1 to n.
For every number:
If it is divisible by 3, print "Fizz"
If it is divisible by 5, print "Buzz"
If it is divisible by both 3 and 5, print "FizzBuzz"
Otherwise, print the number itself."""
n=int(input("Number :"))
for i in range (1,n+1):
    if(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0 and i%5==0):
        print("FizzBuzz")
    else:
        print(i)
"""Create a simple ATM program.
Start with:
balance = 10000
Keep asking the user to choose an option:
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Rules:
1 → Display balance.
2 → Ask deposit amount and add it to balance.
3 → Ask withdrawal amount.
If amount > balance → "Insufficient Balance"
Otherwise deduct it.
4 → Print "Thank you for using ATM" and stop the program using break.
Any other choice → "Invalid Choice" and use continue.
The ATM should keep running until the user selects Exit.
Concepts tested: while, if-elif-else, break, continue, variables, arithmetic, input validation."""
bal=10000
display="""1. Check Balance
2. Deposit
3. Withdraw
4. Exit"""
print(display)
while(True):
        ch=int(input("Choice:"))
        if(ch==1):
            print("Required balance is ",bal)
        elif(ch==2):
            am=int(input("Enter amount you want to deposit"))
            bal = bal + am
            print("Balance after adding",bal)
        elif(ch==3):
            w=int(input("Amount for Withdraw"))
            if(w>bal):
                print("Insufficient Balance")
            else:
                bal -= w
                print("Now bal is",bal)
        elif ch == 4:
            break

        else:
            print("Invalid choice")
            continue
print("Thank you for using ATM")
            
        
      

    
