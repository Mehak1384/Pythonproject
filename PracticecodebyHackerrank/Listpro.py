"""  ""Level 1 (Basic)
Create a list of 5 fruits and print it.
Print the first, last, and third element.
Change the second element.
Add an element using:
append()
insert()
Remove an element using:
remove()
pop()
del
Find the length of a list.
Check whether "Apple" exists in the list.
Print every element using:
for loop
while loop
Reverse a list.
Sort a list in ascending and descending order.""
#Answer
fruit= ['apple','mango','blueberry','strawberry','banana']
print(fruit[0],fruit[4],fruit[-3])
fruit[3]='Cake'#replace a list item using changing the value at a particular index
print(fruit)
#adding the element in list using the append and insert
append_fruit=fruit.append('Cheescake')
insert_fruit=fruit.insert(0,'pasta')
print(fruit)
#delete an element using remove,pop,del
print(fruit.remove('apple'))
print(fruit)
print(fruit.pop(4))
print(fruit)
del fruit[3]
print(fruit)
#length of a list
print(len(fruit))
if 'apple' in fruit:
    print("Yes apple is present in list")
else:
    print("OOPS:)BAD LUCK")
for i in range(len(fruit)):
    print(fruit[i])
i=0
while i < len(fruit):
    print(fruit[i])
    i += 1
print(fruit.sort())
print(fruit)
print(fruit.sort(reverse=True))
print(fruit)"""
"""Find the largest element without using max().
Find the smallest element without using min().
Find the sum of all elements without using sum().
Count how many even numbers are present.
Count how many odd numbers are present.
Remove duplicate elements.
Find the second largest number.
Merge two lists.
Copy a list without affecting the original.
Print elements present at even indexes only."""
num=[5,66,7,0,5]
for i in range (len(num)):
    for j in range(i+1,len(num)):
       if num[i] > num[j]:
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
for i in range(len(num)):    
    print(num[i])
print("The largest number is :",num[4])
print("The smallest number is :",num[0])
print("The second largest number is :",num[3])
num2=["Mehak","Ash","Bhavya"]
print("Merge of 2 list",num+num2)
num3=num2.copy()
print("We have created the list using copy",num3)
count=0
sum=0
for i in range(0,len(num)):
    sum+=num[i]
print("sum of lis",sum)
for i in range(0,len(num)):
    if (num[i]%2==0):
        count+=1
print("Total count of even numbers are ",count)
count_odd=0
for i in range(0,len(num)):
    if (num[i]%2!=0):
        count_odd+=1
print("Total count of Odd numbers are ",count_odd)
for i in range(len(num)-1,-1,-1):
    print(num[i])


