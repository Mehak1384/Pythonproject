"""1. Basic Level — Electricity Bill
Write a Python program to calculate an electricity bill based on units consumed:
If units ≤ 100 → ₹5 per unit
If units > 100 and ≤ 200 → ₹7 per unit
If units > 200 → ₹10 per unit
Take the number of units as input and display the total bill.
Concepts tested: input(), type conversion, if-elif-else, arithmetic operators."""
#Code
unit=int(input("Enter the unit you have consumed "))
display="""If units ≤ 100 → ₹5 per unit
If units > 100 and ≤ 200 → ₹7 per unit
If units > 200 → ₹10 per unit"""
print(display)
if(unit<=100):
    bill=5*unit
    print("Your total bill is :",bill)
elif(unit>100 and unit<=200):
    bill=7*unit
    print("Your total bill is :",bill)
elif(unit>200):
    bill=unit*10
    print("Your total bill is :",bill)
print("Your for visiting on our console based application")
"""2. Intermediate Level — Number Analysis
Write a Python program that takes one positive integer from the user and:
Check whether the number is even or odd.
Check whether it is divisible by 3 and 5.
If it is divisible by both, print "Divisible by both 3 and 5".
Otherwise, print "Not divisible by both".
Then use a loop to calculate the sum of all numbers from 1 to that number."""
n=int(input("Write a one postive number you want to check "))
display="""
Check whether the number is even or odd.
Check whether it is divisible by 3 and 5.
If it is divisible by both, print "Divisible by both 3 and 5"""
print(display)
if (n>0):
    if(n%2==0):
        print(n,"is even")
    else:
        print(n,"is odd")
    if (n%3==0 and n%5==0):
        print(n,"is divisible by 3 and 5")
    else:
        print(n,"is not divisible by 3 and 5")
    sum=0
    for i in range(1,n+1):
        sum+=i
    print("Sum of numbers are :",sum)
else:
    print("Number is not eligble for this code.")
"""3. High Level — Number Guessing Logic

Write a Python program for a simple number guessing game.
The secret number is:
secret = 37
The user gets 5 attempts to guess the number.
For every attempt:
If the guess is greater than the secret number → print "Too High"
If the guess is smaller → print "Too Low"
If the guess is equal → print "Correct!" and stop the game using break.
After 5 unsuccessful attempts, print:
Game Over! The correct number was 37
Extra challenge:
If the user enters 0 or a negative number, print "Invalid Guess" and do not count that attempt.
Concepts tested: while loop,"""
secret=13
at=0
while(at<5):
    guess=int(input("simple number guessing game"))
    if guess <= 0:
        print("Invalid Guess")
        continue
    if(guess==secret):
        print("Correct!")
        break
    elif(guess>secret):
        print("Too High")
        
    elif(guess<secret):
        print("Too Low")
    at+=1
    if(at==5):
        print("Game Over! The correct number was 13")
        break
    
    


