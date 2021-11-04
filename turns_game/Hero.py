
class Hero:
    def __init__(self,hp=10.0,level=1.0,coins=0,damage=2):
        self.hp= hp
        self.damage= damage
        self.level= level
        self.coins= coins

    def constructor_hero():
        print("")
    def heal(hp):
        hp+=hp*0.5
        return hp
        
    def level_up(level,damage,hp,coins):
        #we need to restart hp avery level for the Hero.
        max_add_hp=10
        max_hp=10
        if((coins*1.2) > level):
            m=0.3
            level=level+1
            max_add_hp=(max_add_hp*m)+max_add_hp
            if(max_hp<max_add_hp):
                max_hp=max_add_hp 
            damage=(damage*m)+damage # (2 * 0.3)+2  -> 2.6
            hp=(hp*m)+hp             # (10*0.3) +10 -> 13.3 ->max_add_hp
            hp=max_hp                         #   3.3 +max_add_hp
                                    #    3.3 + 10 
                                    #    13.3 < 15 -> go inside max 15.
            #need to didact the number of coins from hero conins.
            return level,damage,hp,


    def attack_hero():
        print("")
    def defend():
        print("")
    def reduce_health():
        print("")
    def choose_action():
        print("")
    