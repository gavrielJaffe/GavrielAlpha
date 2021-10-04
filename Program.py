def notural(x):
    if ((x%2==0)or(x%3==0)or(x%5==0)or(x%7==0)):
        x="False"
        return x 
    else:
        return True

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

if __name__=="__main__":     
    main()