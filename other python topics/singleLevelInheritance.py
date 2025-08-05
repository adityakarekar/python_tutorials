class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
        
    def male_sound(self):
        return "Animal makes sound boowow"
    
    
    
class Dog(Animal):
    def __init__(self,name,species,breed):
        Animal.__init__(self,name,species)
        self.breed=breed
        
    def make_sound(self):
        return "Dog barks woof woof"
        
    def get_breed(self):
        return self.breed
    
class Cat(Animal):
    def __init__(self,name,species,breed):
        Animal.__init__(self,name,species)
        self.breed=breed
        
    def make_sound(self):
        return "Cat meows meow meow"
            
            
            
dog=Dog("Jonny","dog","retriever")
print(dog.make_sound())

cat=Cat("Kitty","cat","persian")
print(cat.make_sound())
