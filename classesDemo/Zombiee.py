from Enemy import *
class Zombiee(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Zombiee", health_points=health_points, attack_damage=attack_damage)
        
    def talk(self):
        print("Spreads disease")