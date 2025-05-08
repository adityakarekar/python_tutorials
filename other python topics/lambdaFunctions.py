double =lambda x: x * 2
print(double(5))  # Output: 10


cube = lambda x: x ** 3
print(cube(3))  # Output: 27

avg=lambda x,y,z: (x+y+z)/3
print(avg(1,2,3))  # Output: 2.0



def appl(fx,value):
    return 6 +fx(value)

print(appl(lambda x: x ** 3,5)) # Output: 131
#This is a function that takes a function 
# and a value as arguments, 
# applies the function to the value, 
# and adds 6 to the result.