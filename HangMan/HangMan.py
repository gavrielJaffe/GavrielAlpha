import random
from typing import Counter

def main():
    counter=8    
    GuessWords = ("alpha", "is", "great","team")
    rnd=random.randrange(0, 4)
    GameWord=GuessWords[rnd]
    list_guess=["_"] * len(GameWord)
    #as long as the player have life or did not win the game.
    while(( (counter!=0) and (GameWord!="".join(list_guess)))):
        print("your information on the words currntly is: ",list_guess)
        letter=input("entear one of letter between a-z:").lower()
        #  while input invalid,asking for a good input
        while not (letter.isalpha() and len(letter)==1):     
            letter=input("can't be anything else than single english abc letters try again: ").lower()
        #need to put player guss in place ,
        if(letter in GameWord):
                for i in range (len(GameWord)):
                #compare this letter to every guessed by user 
                    if(GameWord[i]==letter):
                       list_guess[i]=letter
                print("The current situation :",list_guess)
        else:
            counter=counter-1
    if(GuessWords=="".join(list_guess)):
        print("good,you got avery thing right")
    elif(counter==0):
        print("you did all of your guss")

if (__name__=="__main__"):  
    main()