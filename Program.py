def main (): 
    sum=1
    for i in range(101): 
        sum+=i
        
        print ("all of number's : ",sum)
        if((i==5)or(i==6)or(i==7)or(i==8)):
            x =azert(i)
            print("the azert of the number is :  ",x,i)


def azert(number):
    prodect=1
    for j in  range (number):
        prodect =prodect * (j+1)
    return prodect

if __name__=="__main__":     
    main()