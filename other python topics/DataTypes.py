#Python Data Types:
#None
#Numeric
#List
#Touple
#Dictionary already covered
#String

#Numeric has further subtypes
#int
#float
#bool
#complex

print(type(1))
print(type(3.142))

# num=a+bj
# normally its a+bi format but here i=j
num=3+5j
print(num)
print(type(num))

# #some type coversion
# a=2
# b=(float)(a)
# print(b)
# # We can do vice-versa
# b=3.14
# a=(int)(b)
# print(a)

# We can also create complex numbers like so
a=10
b=5
c=complex(a,b)
print(c)

#Sequence: List,Set,Tuples,Dictionary,String,Range
lst=["Aditya","Sayali"]
print(type(lst))

tup=('a',"b","c")
print(type(tup))

# Range 
print(list(range(1,10,2)))