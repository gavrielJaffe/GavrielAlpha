
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
        if((coins*1.2) > level):
            m=0.3
            level=level+1
            damage=(damage*m)+damage # (2 * 0.3)+2  -> 2.6
            hp=(hp*m)+hp             # (10*0.3) +10 -> 13.3
            #

        print("")


    def attack_hero():
        print("")
    def defend():
        print("")
    def reduce_health():
        print("")
    def choose_action():
        print("")
    