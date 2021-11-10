

from typing import Counter
from Hero import Hero

from monster import Monster
from Hero import Hero

def main():
    obj_hero=Hero()
    cunt_dead=0
    monster_resat=5

    #need to inized the moster
    obj_monster=Monster(x,y,z,"bogis")
    obj_hero.choose_action(obj_hero,obj_monster)
    if (obj_monster.monster_hp<0):
        cunt_dead=cunt_dead+1
        #creating a new moster stronger.
        obj_monster=Monster(monster_resat+cunt_dead,monster_resat+cunt_dead,monster_resat+cunt_dead)
        #attack the hero.
        obj_monster.attack(obj_hero,obj_monster)
        


        print ("hi from 13")
    print(obj_hero,"obj hero")
    if(__name__=="__main__"):
        main()