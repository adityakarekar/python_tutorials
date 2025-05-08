class Person:
    def __init__(self, name="Jasmine",age=24,address="Oklahoma,US"):
        print("Hey I am a person")
        #Function to initialize the object.
        #Gets called when the object is created.
        self.name=name
        self.age=age
        self.address=address


    def info(self):
        print(f"{self.name} is {self.age} years old and lives in {self.address}.")

person = Person("Aditya Karekar", 25, "Pune")
person.info()

person2= Person("John Doe", 30, "New York")
person2.info()
person3= Person("Rashmi")
person3.info() #Output: Hey I am a person
