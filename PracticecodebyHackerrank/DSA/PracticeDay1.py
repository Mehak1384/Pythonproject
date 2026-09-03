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

