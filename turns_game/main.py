

from Hero import Hero

from monster import Monster



def main():
    # as long as the Hero is alive need to chose to attack or to defend. , 

    obj_hero=Hero(10,10,1,1)
    obj_monster=Monster(5,5,1,"bogi")
# (obj_hero.heal!=0)
    answer=input("you can chose to attack or to deffed,for attack press 1 ,to deffend press 2.\n")
    answer=int (answer)
    while not((answer==1)or(answer==2)):
        answer=input("you can chocse to attack or to deffed,for attack press 1 ,to deffend press 2.\n")
        answer=int(answer)
        if(answer==1):
        #make some action on attacking.
            obj_hero.attack_hero()
        elif(answer==2):
        #make some action on deffeding.
            obj_monster.attack_hero()




    print("ok we gut till 16.")        



    if(__name__=="__main__"):
        main()
