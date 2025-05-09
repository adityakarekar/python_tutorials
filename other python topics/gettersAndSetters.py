class MyClass:
    def __init__(self,value):
        self._value = value
        

    @property
    def time_ten_value(self):
        return self._value * 10
    

    @time_ten_value.setter
    def time_ten_value(self,new_value):
        self._value = new_value / 10

    def show(self):
        return f"Value: {self._value}, Time Ten Value: {self.time_ten_value}"



my_obj=MyClass(5)
print(my_obj.time_ten_value) # This will call the getter method
my_obj.time_ten_value = 100 # This will call the setter method
print(my_obj.time_ten_value) # This will call the getter method
print(my_obj.show()) # This will call the show method