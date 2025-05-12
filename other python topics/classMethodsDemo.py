class Employee:
    company = "TechCorp"  # Class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"Employee works at {self.company}. His/Her name is {self.name} with salary {self.salary}.")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @classmethod
    def from_string(cls, emp_str):
        return cls(emp_str.split("-")[0],int(emp_str.split("-")[1]))
    #This code acts as a constructor and creates an instance of the class using the string passed to it.


    
e1 = Employee("Alice",50000)
e1.change_company("NewTech")  # Change class variable using class method
str1="Aditya-60000"
e2=Employee.from_string(str1)  # Create instance using class method
e2.show()  # Show employee details


x=[1,2,3]
print(dir(x))
print(x.__add__)


class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age


p=Person("John", 30)
print(p.__dict__)  # Print instance variables

print(help(Person))