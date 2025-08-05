class Employee:
    def __init__(self,name):
        self.name=name
        
    def show(self):
        return f"{self.name} is an employee"
        
        
class Dancer:
    def __init__(self,style):
        self.style=style
        
    def dance(self):
        return f"{self.name} dances in {self.style} style"
    
    def show(self):
        return f"{self.name} is a dancer"
    
    
class DancerEmployee(Dancer,Employee):
    def __init__(self,name,style,choreographer):
        Employee.__init__(self,name)
        Dancer.__init__(self,style)
        self.choreographer=choreographer
        
        
    def perform(self):
        return f"{self.name} performs a {self.style} dance choreographed by {self.choreographer}"
    
    
employee=Employee("Alice")
dancer=Dancer("Ballet")
dancer_employee=DancerEmployee("Bob", "Hip Hop", "Charlie")
print(dancer_employee.perform())
print(dancer_employee.dance())
print(dancer_employee.show())
print(DancerEmployee.mro())