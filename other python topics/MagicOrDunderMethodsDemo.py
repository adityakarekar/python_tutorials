class Employee:
    name="Aditya"
    
    def __init__(self,name):
        self.name=name
    
    def __len__(self):
        i=0
        for c in self.name:
            i+=1
        return i
    
    def printName(self):
        return self.name

    # String representation
    def __str__(self):
        return f"Employee name is {self.name}"
    
    # Official representation
    def __repr__(self):
        return f"Employee('{self.name}')"
    
    def __call__(self):
        return f"Hello  Cool Guy!!"
        
    
e=Employee("Aditya")
print(e.printName())
# print(e.name)
# print(len(e))
