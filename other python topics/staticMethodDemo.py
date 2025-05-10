class Math:
    def __init__(self,value):
        self.value=value

    def add_to_value(self, x):
        self.value += x
        return self.value
    
    @staticmethod 
    # This is a static method
    # It can be called without creating an instance of the class
    def add(x, y):
        return x + y
    

m=Math(10)
print(m.add_to_value(5))  # Output: 15
print(Math.add(5, 10))  # Output: 15
print(m.add(5, 10))  # Output: 15

        