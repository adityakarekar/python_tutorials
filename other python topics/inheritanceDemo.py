class Employee:
    def __init__(self,name,emp_id):
        self._name=name
        self._emp_id=emp_id
    def show(self):
        return f"Name: {self._name}, Employee ID: {self._emp_id}"
    

class Prgrammer(Employee):
    def showLanguage(self,_language="Python"):
        return f"Name: {self._name}, Employee ID: {self._emp_id}, Language: {_language}"
    


e=Employee("John", 101)
p=Prgrammer("Doe", 102)
print(p.show())
print(p.showLanguage("Java"))