import random
class Monster:
    def __init__(self,monster_name,monster_hp,monster_damage,monster_level):
        self.monster_name=monster_name
        self.monster_hp=monster_hp
        self.monster_damage= monster_damage
        self.monster_level=monster_level

    def constructor_monster(monster_name,hero,monster):
        # get level of monster.
        #  rnd=monster.monster_level
        rnd=hero.level
        rnd=random(rnd (-1) ,rnd (+1))
        monster.monster_damage=monster.monster_level*(0.30)
        return monster.monster_damage
        
    def attack(self,hero,monster):
        #reduce health to the hero.
        print("got inside of attack in 20")
        #need to get answer from choose.
        hero.reduce_health(self,answer)
        
       
    def reduce_health_monster(self,hero):
        #reduce health to monster.
        self.monster_hp = hero.damage - self.monster_hp
        if (self.monster_hp<=0):
            self.monster_hp=0
            #do we need to create a new monster hear ? 
        return self.monster_hp

    