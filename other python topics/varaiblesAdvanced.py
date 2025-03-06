a=10
b=a
# id(variable):Is used to get the 
# address of the variable
print(id(a))
print(id(b))
print(id(10))

a=9
print(id(a))
print(a==b)

# In python we cannot have a variable as constant
print(type(a))