from Person import *
class Student(Person):
    def __init__(self, name, age,degree):
        super().__init__(name, age)
        self.degree=degree
        