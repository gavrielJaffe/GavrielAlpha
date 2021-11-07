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
    def defend():
        print("")
    def reduce_health():
        print("")
    def choose_action(hero):
        answer=input("1:attack,2:lever up,3:heal ,4:defend")
        answer=int(answer)
        while not(answer.isdigit)&((1<=answer<=4)):
            answer=input("1:attack,2:lever up,3:heal ,4:defend")
            answer=int(answer)
        hero.conins=hero.conins+1
