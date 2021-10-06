 import re

def main():
   number=input("To add a product click 1,for Deleting a product click 2, to cart click 3 ")
   while((number!="3")):
        print("type is : ",type(number))
        #Add a product   
        if(number=="1"):
            #get name of Product 
            product=input("enter name of product: ")
            #get price in 'int' only 
            price=input("enter price of product: ") 
            while not(price.isdigit()):
                price=input("enter price of product: ") 
            #get unit number 'int' only    
            unit=input("enter unit number to purchase: ")
            while not( unit.isdigit()):
                unit=input("enter unit number to purchase: ")
            

            
    #dic={"penter roductName":"price","unit" } 


            print("adding")
            break
        #delete a product     
        elif(number=="2"):
            print("deleting")
            break
        #end of shopping     
        elif(number=="3"):
            break
        else:
            number=input("could be numbers only 1,2,3 , To add a product click 1,for Deleting a product click 2, to cart click 3:  ")

if __name__=='__main__':
    main()

#   thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "year": 2020 }
                       
#     print(thisdict)


