class Employee:
    # class variable
    company = "Google"
    
    def __init__(self, name,raise_amt):
        # instance variable
        self.name = name
        self.raise_amt = raise_amt
        
    def show(self):
        print(f"Name: {self.name}, Company: {self.company}")



e1 = Employee("Alice", 1.5)
Employee.company = "Microsoft"  # changing class variable
e1.show()
e2 = Employee("Bob", 2.0)
e2.show()