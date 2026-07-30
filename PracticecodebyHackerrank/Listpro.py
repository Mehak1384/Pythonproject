"""Level 1 (Basic)
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
Sort a list in ascending and descending order."""
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
print(fruit)