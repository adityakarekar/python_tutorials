class Employee:
    def __init__(self):
        self.__name = "Alice"

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name=name

    def _sayHello(self):
        print("Hello")


a=Employee()
print(a._Employee__name)  # another way to access private variable
print(a.get_name())
a.set_name("Bob")
print(a.get_name())

print(a.__dir__())

#a.__ClassName__private_field  # this is called name mangling

class Employee2(Employee):
    def  __init__(self,):
        self.__occupation="Engineer"

    def get_occupation(self):
        return self.__occupation
    



b=Employee2()
print(b.get_occupation())
b._sayHello() #sayHello is protected method, so it can be accessed in child class
        



