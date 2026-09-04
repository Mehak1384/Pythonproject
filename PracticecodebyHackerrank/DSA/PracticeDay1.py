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
if index>=0 and index<len((arr)):
    print(arr[index])
else:
   print("Sorry we can find the value for the given index",index)
"""Q3. Index and Value
Given:
arr = [10, 20, 30, 40, 50]
Traverse the list and print:
Index 0 -> 10
Index 1 -> 20
Index 2 -> 30
Index 3 -> 40
Index 4 -> 50"""
arr = [10, 20, 30, 40, 50]
for i in range(len(arr)):
    print("Index",i,"->",arr[i])
"""Write a program to traverse:
arr = [12, 24, 36, 48, 60]
and print every element without using its index."""
arr = [12, 24, 36, 48, 60]
for elements in arr:
    print(elements)
"""Q5.Find the Largest Element ⭐
Given:

arr = [12, 45, 7, 89, 34]

Find and print the largest element.

Restrictions:

Don't use max()
Use a loop."""
arr=[12,54,7,89,34]
max_n=0
for i in range(len(arr)):
        if max_n<arr[i]:
            max_n=arr[i]
        
print(max_n)
"""Q4. Find the Smallest Element ⭐
Given:

arr = [25, 8, 42, 3, 19]

Find and print the smallest element.

Restrictions:

Don't use min()
Use a loop."""
arr = [25, 8, 42, 3, 19]
min_n=arr[0]
for i in range(len(arr)):
        if min_n>arr[i]:
            min_n=arr[i]
        
print(min_n)
"""Q5. Count Even and Odd Elements ⭐
Take n integers from the user and count how many elements are even and how many are odd."""
n=int(input("Enter the elemensr you wan to check "))
arr=[0]*n
for i in range(len(arr)):
    arr[i]=int(input())
count=0
count_odd=0
for i in range(len(arr)):
    if(arr[i]%2!=0):
        count+=1
    else:
        count_odd+=1
print(count,count_odd)
for i in range(len(arr)):
    print(i,arr[i])
"""Q6. Search for an Element 🔍
Given:
arr = [10, 25, 7, 40, 15]
Take a number from the user and check whether that number exists in the array.
Expected behavior:
Enter number: 40
40 found
If the number doesn't exist:
Enter number: 50
50 not found
Restrictions:
Use a loop.
Don't use in.
Don't use index()."""
arr = [10, 25, 7, 40, 15]
n=int(input("Enter the number you want to search"))
for i in range(len(arr)):
    if (arr[i]==n):
        print("Number found",n)
        break  
else:
    print(n,"Number not found")
"""Q7. Count Occurrences 
Given:
arr = [10, 20, 10, 30, 10, 40, 20]
Take a number from the user and count how many times it appears in the array.
Example:
Enter number: 10
10 occurs 3 times"""
arr = [10, 20, 10, 30, 10, 40, 20]
n=int(input("Enter the number from the user"))
count=0
for i in range(len(arr)):
    if(arr[i]==n):
        count+=1
print(n,"occured",count,"times")
"""Q8. Find the Position of an Element 🔍
Given:
arr = [15, 30, 45, 60, 75]
Take a number from the user and find its index.
Example:
Enter number: 45
45 found at index 2
If it doesn't exist:
Enter number: 50
50 not found"""
arr = [15, 30, 45, 60, 75]
n=int(input("Enter the number you want to find"))
for i in range(len(arr)):
    if(arr[i]==n):
        print(n,"found at index",i)
        break
else:
    print(n,"not found")
"""Q9. Find the Second Largest Element ⭐⭐

Given:
arr = [12, 45, 7, 89, 34]
Find and print the second largest element.
Expected output:

Second largest = 45
Restrictions:
Don't use sort().
Don't use max().
Use loops.
Try to solve it without creating another array."""
arr = [12, 45, 7, 8900, 340]

largest = arr[0]
second_largest = arr[0]

for i in range(1, len(arr)):

    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]

    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print("Second largest =", second_largest)