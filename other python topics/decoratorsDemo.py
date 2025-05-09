def greet(func):
    def wrapper(*args, **kwargs): # This allows the wrapper to accept any number of positional and keyword arguments
        print("Hello!")
        func(*args, **kwargs) # Call the original function with its arguments
        print("Goodbye!")
    return wrapper


@greet # What this does is equivalent to hello = greet(hello)
def hello():
    print("Hello, World!")

hello()
print("-----------------------")

@greet 
def add(a,b):
    print(a+b)

add(2,3)
