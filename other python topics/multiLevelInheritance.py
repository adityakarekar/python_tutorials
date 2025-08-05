class GrandParent:
    def __init__(self,name):
        self.name=name
        
    def walk(self):
        return f"Grandpa: {self.name} is walking"
    
    def move(self):
        return "Moving"
    
class Parent(GrandParent):
    def __init__(self,name,age):
        GrandParent.__init__(self,name)
        self.age=age
        
        
    def talk(self):
        return f"Parent: {self.name} is talking at age {self.age}" 
    
    def move(self):
        return "Moving faster than grandparent"
    
    
class Child(Parent):
    def __init__(self,name,age,grade):
        Parent.__init__(self,name,age)
        self.grade=grade
        
    def study(self):
        return f"Child: {self.name} is studying in grade {self.grade}"
    
    def play(self):
        return f"Child: {self.name} is playing"
    


grandparent = GrandParent("John")
print(grandparent.walk())

parent=Parent("Mike",50)
parent.talk()
parent.move()


child=Child("Lucy",10,5)
print(child.study())
print(child.play())
print(child.move())