def main():
   PriceInCart = 0
   all_products={}
   flag=4  
   oldquantity =0
   while((flag!="3")):
        flag=input("To add a product click 1,Deleting a product click 2, to cart click 3:")   
        if(flag=="1"):
            #get name of Product,price and quantity in 'int' only 
            
            product_name=input("enter name of product:")
            price=input("enter price of product: ") 
            while not(price.isdigit()):
                price=input("enter price of product: ") 
            quantity=input("enter quantity number to purchase:")
            while not( quantity.isdigit()):
                quantity=input("enter quantity number to purchase: ")

            print("all_products",all_products) 
            print("new product: ",product_name) 
                    
            if (product_name in all_products):
                print("going inside")
                oldquantity +=int(quantity)
                all_products[product_name]["unit_number"]=oldquantity
                print("quantity",quantity)
                print("oldquantity",oldquantity)
                PriceInCart = int(all_products[product_name]["unit_number"])*int( all_products[product_name]["price_prodct"] )
                print(all_products[product_name]["unit_number"])
                print("all_products",all_products) 

                
                print("price in cart",PriceInCart)
            else:
                all_products[product_name]={"price_prodct":price,"unit_number":quantity}
                oldquantity=0
                all_products[product_name] = {"price_prodct":price,"unit_number":quantity}
                teamp_q = all_products[product_name]["unit_number"]
                teamp_p = all_products[product_name]["price_prodct"]
                print("all_products",all_products)
                PriceInCart+=int(teamp_q)*int(teamp_p)
                print("price is cart : ",PriceInCart)     
        elif(flag=="2"):
            if(all_products=={}):
                print("no product in your cart")
                continue
            prodact_remove = input("enter the prodect you want to remove?\n")
            if(prodact_remove in all_products):
                prodact_quantity_remove = int(input("how meny item you want to remove from it?\n"))
                if(prodact_quantity_remove<0):
                    print("you enter invalid number")
                elif(prodact_quantity_remove >= int(all_products[prodact_remove]["unit_number"])):
                     PriceInCart-= int(all_products[prodact_remove]["unit_number"])*int(all_products[prodact_remove]["price_prodct"])
                     del all_products[prodact_remove]
                     print(all_products)
                else:
                    all_products[prodact_remove]["unit_number"] = int(all_products[prodact_remove]["unit_number"])- prodact_quantity_remove
                    PriceInCart=PriceInCart-(int(all_products[prodact_remove]["unit_number"])*int(all_products[prodact_remove]["price_prodct"]))
                    print(all_products)
            else:
                 all_products[prodact_remove]["unit_number"] = int(all_products[prodact_remove]["unit_number"]) - prodact_quantity_remove
                 PriceInCart= PriceInCart-int(all_products[prodact_remove]["unit_number"])*int(all_products[prodact_remove]["price_prodct"])
                 print(all_products)

            print(PriceInCart)
        #end of shopping     
        elif(flag=="3"):
            break
        
if __name__=='__main__':
    main()
