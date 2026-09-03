"""Q1. Create and Traverse
Write a Python program to:
Take n integers from the user.
Store them in a list.
Traverse the list using an index.
Print every element.
Restriction: Don't use for element in arr."""
n=int(input("How many elements you want to enter in the array"))
arr=[0]*n
print("Creation of an array:")
for i in range(n):
    arr[i]=int(input())
print("Traverse of an array")
for i in range(n):
    print(i,arr[i])
"""Q2. Access by Index
Given:
arr = [15, 25, 35, 45, 55]
Write a program that:
Takes an index from the user.
Prints the element at that index.
Handles an invalid index without crashing."""
arr = [15, 25, 35, 45, 55]
index=int(input("Please provide us index you want to print"))
if index==0:
    print(arr[index])
elif index==1:
    print(arr[index])
elif index==2:
    print(arr[index])
elif index==3:
    print(arr[index])
elif index==4:
    print(arr[index])
else :
    print("Sorry we can find the value for the given index",index)
