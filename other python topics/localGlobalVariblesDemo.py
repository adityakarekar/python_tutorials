x=10

def my_function():
    global x # Declare x as global
    x=20 # This will create a new local variable x
    print(x) # This will print the local x

my_function()
print(x) # This will print the global x
# The output of the above code will be: