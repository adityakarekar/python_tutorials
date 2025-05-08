from functools import reduce


cube=lambda x: x**3

list1=[1,2,3,4,5]

list2=list(map(cube,list1))
#or
# list2=list(map(lambda x:x**3,list1))


#Gives the cube of each element 
# in list1 and stores it in list2
print(list2)

list3=[1,2,3,5,7,9,11,13,15,17,19]
list4=list(filter(lambda x: x%3==0,list3))
#Gives the numbers divisible by 3 in list3 and stores it in list4
print(list4)


list5=[1,2,3,4,5,6,7,8,9,10]
list6=reduce(lambda x,y:x*y,list5)
#Gives the sum of all elements 
# in list5 and stores it in list6
print(list6)