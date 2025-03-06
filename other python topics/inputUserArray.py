from array import *
arr=array("i",[])
n=int(input("Enter the length of the array: "))
for i in range(n):
    x=int(input("Enter the next value: "))
    arr.append(x)
print(arr)

key=int(input("Enter a value to search: "))
k=0
for e in arr:
    if e==key:
        print(k)
        break

    k+=1
