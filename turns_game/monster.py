
from _typeshed import Self
import random
from Hero import Hero 
class Monster:
    def __init__(self):
        self.monster_name= self.monster_name
        self.monster_hp=self.monster_hp
        self.monster_damage= self.monster_damage
        self.monster_level=self.monster_level

    def constructor_monster(monster_name,hero,monster):
        # get level of monster.
        #  rnd=monster.monster_level
        rnd=hero.level
        rnd=random(rnd (-1) ,rnd (+1))
        monster.monster_damage=monster.monster_level*(0.30)
        return monster.monster_damage
        print("")
    def attack_monster(hero,monster):
        #need to reduce helth monster to the hero.or monster to hero.
        monster.reduce_health_monster()
        print("")
    def reduce_health_monster(hero,monster):
        monster.monster_hp = hero.damage - monster.hp
        if (monster.monster_hp<=0):
            monster.monster_hp=0
            #do we need to create a new monster hear ? 
        return monster.monster_hp

    