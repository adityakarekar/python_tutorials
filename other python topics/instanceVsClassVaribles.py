class Employee:
    # class variable
    company = "Google"
    no_of_employees = 0
    
    def __init__(self, name,raise_amt):
        # instance variable
        Employee.no_of_employees += 1
        self.name = name
        self.raise_amt = raise_amt
        
    def show(self):
        print(f"Name: {self.name}, Company: {self.company}, company Size: {self.no_of_employees}, Raise Amount: {self.raise_amt}")



e1 = Employee("Alice", 1.5)
Employee.company = "Microsoft"  # changing class variable
e1.show()
e2 = Employee("Bob", 2.0)
e2.show()