

from Hero import Hero

from monster import Monster
from Hero import Hero

def main():
    obj_hero=Hero(10,10,1,1)
    obj_monster=Monster(5,5,1,"bogis")
    obj_hero.choose_action(obj_hero,obj_monster)
    if (obj_monster.monster_hp<0):
        



    print(obj_hero,"obj hero")
    print ("hi from 13")
    if(__name__=="__main__"):
        main()
    # answer=input("hero's acton -1:attack,2:lever up,3:heal ,4:defend")
    # answer=int (answer)
    # while not((answer==1)or(answer==2)):
    #     answer=input("hero's acton -1:attack,2:lever up,3:heal ,4:defend\n")
    #     answer=int(answer)