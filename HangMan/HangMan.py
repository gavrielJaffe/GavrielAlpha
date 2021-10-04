import random

def fun():{

}


def main():    
    GuessWords = ["alpha", "is", "great","team"]
    print ("words",GuessWords)
    rnd=random.randrange(0, 4)
    GameWord=GuessWords[rnd]
    size=len(GameWord)
    underLine = "_" * size
    for i in range(8):
        print("your information on the words currntly is  : ",underLine)
#ניתן להפו לפונקיצה אחת בודקת ומחזירה לחסוך בזמן ולא  בתור פור?נקודה למחשבה -יעילות
        print("entear a lette between a-z: ")
        letter=input()
        while(letter.isalpha()):        
            print("can't be anything else than english abc letters")
            letter=input()
        print("Great it was between the abc letters ")
        






if(__name__=="__main__"):
    main()
