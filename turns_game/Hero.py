global max_add_hp
max_add_hp=10.0

class Hero:
    def __init__(self,hp=10.0,level=1.0,coins=0.0,damage=2.0):
        self.hp= hp
        self.damage= damage
        self.level= level
        self.coins= coins   
    def constructor_hero():
        print("")
    def heal(hp):
        hp+=hp*0.5
        return hp
               # 10,  1,     4,   2    
    def level_up(hp,level,coins,damage):
        global max_add_hp
        if((coins*1.2) > level):
            m=0.3
            level=level+1
            max_add_hp=(max_add_hp*m)+max_add_hp # (10*0.3) +10 -> 13.3 ->max_add_hp
            damage=(damage*m)+damage # (2 * 0.3)+2  -> 2.6  ;>damage
            #restart hp avery level for the Hero.
            hp=max_add_hp                        
            coins=coins*0.5
            return [hp,level,coins,damage]#return list of new values.
    def hero_attack(monster,hero):
        #hero reduce_health to the monster. hero_attack & reduce_health are connected .
        hero.reduce_health()
        if(monster.moster_hp<=0):
            coins=hero.coins + hero.level
        return coins
    def defend(hero,monster):
        # reduce_health but not as much like regular.
        hero.hp= hero.hp-(monster.damage*0.2)
        #10       10    - (10*0.2=>2)
        print ("hero's hp after the attack is :",hero.hp)   
    def reduce_health(monster,hero,answer):
        #reduce health to the hero ,
        if(answer==4):
            return hero.defend(monster,hero)
        hero.hp=monster.damage-hero.hp
        #return hero's life back 
        return print ("hero's hp after the attack is :",hero.hp)
    def choose_action(hero,moster):
        answer=input("1:attack,2:lever up,3:heal ,4:defend")
        answer=int(answer)
        while not(answer.isdigit)&((1<=answer<=4)):
            answer=input("1:attack,2:lever up,3:heal ,4:defend")
            answer=int(answer)
        hero.conins=hero.conins+1
        return moster,hero 
