"""n=int(input("Enter the number of elements in the array"))
arr=[0]*n
for i in range(len(arr)):
    arr[i]=int(input())
sum=0
for i in range(len(arr)):
    sum+=arr[i]
print("Sum of the elements in the array is ",sum)
avg=0
for i in range(len(arr)):
    avg+=arr[i]
avg/=len(arr)
print("Average of the elments in the array is ",avg)
n=int(input("Enter the number of elements in the array"))
arr=[0]*n
for i in range(len(arr)):
    arr[i]=int(input())
count_p=0
count_n=0
count_z=0
for i in range(len(arr)):
    if(arr[i]>0):
        count_p+=1
    elif(arr[i]<0):
        count_n+=1
    else:
        count_z+=1
print("+VE Count is ",count_p)
print("-VE Count is ",count_n)
print("Zero Count is ",count_z)
n=int(input("Enter the number of elements in the array"))
arr=[0]*n
for i in range(len(arr)):
    arr[i]=int(input())
a=int(input("whose first occurence you want to find:"))
for i in range(len(arr)):
    if(arr[i]==a):
        print("First occurence of ",a," is at index ",i)
        break
else:
    print("Element not found")
n=int(input("Enter the number of elements in the array"))
arr=[0]*n
for i in range(len(arr)):
    arr[i]=int(input())
minn=arr[0]
maxx=arr[0]
for i in range(len(arr)):
    if(arr[i]<minn):
        minn=arr[i]
    if(arr[i]>maxx):
        maxx=arr[i]
print("Minimum element in the array is ",minn)
print("Maximum element in the array is ",maxx)
n=int(input("Enter the number of elements in the array"))
arr=[0]*n
for i in range(len(arr)):
    arr[i]=int(input())
for i in range(len(arr)-1,-1,-1):
    print(arr[i])
n=int(input("Enter the number of elements in the array"))"""
n=int(input("Enter the number of elements in the array"))
arr=[0]*n
for i in range(len(arr)):
    arr[i]=int(input())
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=tempg
print("Sorted array is ",arr)