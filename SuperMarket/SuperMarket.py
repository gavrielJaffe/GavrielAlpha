def add_prodact(all_products,new_product):
    all_products[len(all_products)+1]=new_product
#dic is pass by refrence, no need for return 



    
def main():
   PriceInCart = 0
   number=input("To add a product click 1,for Deleting a product click 2, to cart click 3 ")
   all_products={}
   while((number!="3")):
        #Add a product   
        if(number=="1"):
            #get name of Product,price and quantity in 'int' only    
            product_name=input("enter name of product: ")
            price=input("enter price of product: ") 
            while not(price.isdigit()):
                price=input("enter price of product: ") 
            quantity=input("enter quantity number to purchase:")
            while not( quantity.isdigit()):
                quantity=input("enter quantity number to purchase: ")

            if (product_name in all_products):
                print("you have this product alredy  25\n")
            new_product={"name" :product_name, "price_prodct":price,"unit_number":quantity}            
            add_prodact(all_products,new_product)
            if (product_name in new_product):
                print("you have this product alredy 30\n")
            break
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



