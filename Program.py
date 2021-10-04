def notural(x):
    if ((x%2==0)or(x%3==0)or(x%5==0)or(x%7==0)):
        x="False"
        return x 
    else:
        return True

def azert(number):
    prodect=1
    for j in  range (number):
        prodect =prodect * (j+1)
    return prodect

def main (): 
    sum=1
    
    for i in range(101) : 
        sum+=i   
print ("all of number's : ",sum)
print("for 5 we get ", notural(5))
print("for the number 6:" ,notural(6))
print("for the number 7"  ,notural(7))
print("for the number 14" ,notural(14))
print("for the number 152",notural(152))
print("for the number 60693",notural(60693))     
for i in range(101): 
    sum+=i
    print ("all of number's : ",sum)
        
    if((i==5)or(i==6)or(i==7)or(i==8)):
        x =azert(i)
        print("the azert of the number is :  ",x,i)


if __name__=="__main__":     
    main()