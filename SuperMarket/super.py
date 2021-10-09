def main():
   PriceInCart = 0
   all_products={}
   flag=4   
   while((flag!="3")):
        flag=input("To add a product click 1,for Deleting a product click 2, to cart click 3:")   
        if(flag=="1"):
            #get name of Product,price and quantity in 'int' only 
            
            product_name=input("enter name of product:")
            price=input("enter price of product: ") 
            while not(price.isdigit()):
                price=input("enter price of product: ") 
            quantity=input("enter quantity number to purchase:")
            while not( quantity.isdigit()):
                quantity=input("enter quantity number to purchase: ")

            all_products[product_name]={"price_prodct":price,"unit_number":quantity}

            print("all_products",all_products) 
            print("new product: ",product_name) 
                    
            if (product_name in all_products):
                #we need to get quantity in new product and chenge it.no need for price or name agin.
            #   some beg in this line : need to save the old "quantity" and not go over it .
                # all_products[product_name]["unit_number"]+=quantity
                quantity+=all_products[product_name]["unit_number"]
                print("quantity",quantity)
                print(all_products[product_name]["unit_number"])
                teamp_p = int( all_products[product_name]["unit_number"] )
                teamp_q = int( all_products[product_name]["price_prodct"] )
            
                print("teamp_q:",teamp_q)
                print("teamp_p:",teamp_p)
                PriceInCart+=teamp_q*teamp_p
                print("price in cart",PriceInCart)
            else:
                all_products[product_name] = {"price_prodct":price,"unit_number":quantity}
                teamp_q = all_products[product_name]["unit_number"]
                teamp_p = all_products[product_name]["price_prodct"]
                PriceInCart+=int(teamp_q)*int(teamp_p)
                print("price is cart : ",PriceInCart)     
        elif(flag=="2"):
            print("deleting")
            break
        #end of shopping     
        elif(flag=="3"):
            break
        
if __name__=='__main__':
    main()
