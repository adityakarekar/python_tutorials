from Enemy import *
import random
random
class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Ogre", health_points=health_points, attack_damage=attack_damage)
        
        
        
    def talk(self):
        print("grumbling")
        
    def attack(self):
        print("tossing rocks")
        
    def special_attack(self):
        didSpecialAttackWork=random.random() < 0.2
        if(didSpecialAttackWork):
            self.attack_damage+=4
            print("ogre attack damage increased to 4 points")