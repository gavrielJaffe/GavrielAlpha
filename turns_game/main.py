from monster import Monster
from Hero import Hero

def main():
    cunt_dead=0
    monster_reset=5

    obj_hero=Hero()
    obj_monster=Monster(monster_reset,monster_reset,monster_reset,"bogis")
    print(obj_hero,"obj hero")
    while( obj_hero.hp!= 0 ):
        obj_hero.choose_action(obj_hero,obj_monster)
        if (obj_monster.monster_hp<0):
            cunt_dead=cunt_dead+1
            #creating a new moster, stronger.
            obj_monster=Monster(monster_reset+cunt_dead,monster_reset+cunt_dead,monster_reset+cunt_dead)
        #attack the hero.
        obj_monster.attack(obj_hero,obj_monster)
        if(obj_hero.hp<=0):
            print("you lost in the game")
            break
    if(__name__=="__main__"):
        main()