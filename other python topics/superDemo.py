class Employee:
    def __init__(self, name,id,age,address):
        self.name=name
        self.id=id
        self.age=age
        self.address=address

    def show_employee_data(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")


class Programmer(Employee):
    def __init__(self, name, id, age, address, lang):
        super().__init__(name, id, age, address)
        self.lang=lang

    def print_employee_data(self):
        super().show_employee_data()
        print(f"Language: {self.lang}")


programmer=Programmer("Aditya",1,26,"Pune Maharahstra","fastAPI")
programmer.print_employee_data()