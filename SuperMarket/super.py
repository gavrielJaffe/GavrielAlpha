def main():
   price_in_cart = 0
   all_products={}
   flag=4  
   while((flag!="3")):
        flag=input("To add a product click 1,Deleting a product click 2, to cart click 3:")   
        if(flag=="1"):
            #get name of Product,price and quantity in 'int' only 
            product_name=input("enter name of product:")
            price=input("enter price of product: ") 
            while not(price.isdigit()):
                price=input("enter price of product: ")
            price=int(price)
            quantity=input("enter quantity number to purchase:")
            while not( quantity.isdigit()):
                quantity=input("enter quantity number to purchase: ")
            quantity=int(quantity)
            print("all_products",all_products) 
            print("new product: ",product_name)        
            if (product_name in all_products):
                price_in_cart +=quantity*all_products[product_name]["price_product"]     
                all_products[product_name]["unit_number"]=all_products[product_name]["unit_number"]+ quantity
                print("all_products",all_products) 
                print("price in cart",price_in_cart)
            else:
                all_products[product_name]={"price_product":price,"unit_number":quantity}
                print("all_products",all_products)
                #price_in_cart=price * quantity
                price_in_cart+=all_products[product_name]["unit_number"]*all_products[product_name]["price_product"]
                print("price is cart : ",price_in_cart)     
        elif(flag=="2"):
            if(all_products=={}):
                print("no product in your cart")
                continue
            product_remove = input("enter the product you want to remove?\n")
            if(product_remove in all_products):
                product_quantity_remove = input("how meany item you want to remove from it?\n")
                product_quantity_remove =int(product_quantity_remove)
                if(product_quantity_remove<0):
                    print("you enter invalid number")
                elif(product_quantity_remove >= all_products[product_remove]["unit_number"]):
                     price_in_cart-= all_products[product_remove]["unit_number"]*all_products[product_remove]["price_product"]
                     del all_products[product_remove]
                     print(all_products)
                     print("price is cart : ",price_in_cart)
                else:
                    all_products[product_remove]["unit_number"] = all_products[product_remove]["unit_number"]- product_quantity_remove
                    price_in_cart=price_in_cart-product_quantity_remove*all_products[product_remove]["price_product"]
                    print(all_products)
                    print("price is cart : ",price_in_cart)
            else:
                print("price is cart : ",price_in_cart)     
                print("item no in cart")       
if __name__=='__main__':
    main()
