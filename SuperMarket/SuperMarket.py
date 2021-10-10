def add_prodact(all_products,new_product):
    all_products[len(all_products)+1]=new_product
#dic is pass by refrence, no need for return 

def main():
   PriceInCart = 0
   flag=input("To add a product click 1,for Deleting a product click 2, to cart click 3 ")
   all_products={}
   while((flag!="3")):
        #Add a product   
        if(flag=="1"):
            #get name of Product,price and quantity in 'int' only    
            product_name=input("enter name of product: ")
            price=input("enter price of product: ") 
            while not(price.isdigit()):
                price=input("enter price of product: ") 
            quantity=input("enter quantity number to purchase:")
            while not( quantity.isdigit()):
                quantity=input("enter quantity number to purchase: ")

            new_product={"name" :product_name, "price_prodct":price,"unit_number":quantity} 
            new_product2={"name" :"bizzli", "price_prodct":"5","unit_number":"1"} 
            print("new product: ",new_product2)           
            print("new product: ",new_product)           
            add_prodact(all_products,new_product)
                        
            if (product_name in all_products):
                #we need to get quantity in new product  and chenge it.no need for price or name agin. 
                all_products[new_product]["unit_number"]+=quantity
                PriceInCart=all_products[product_name]["unit_number"]*all_products[product_name]["price"]
            else:
                all_products[product_name] = {"price_prodct":price,"unit_number":quantity}
                teamp_q =all_products[product_name]["unit_number"]
                teamp_p=all_products[product_name]["price_prodct"]
                PriceInCart+=int(teamp_q)*int(teamp_p)
                print("price is cart : ",PriceInCart)
                flag=4       
        elif(flag=="2"):
            print("deleting")
            break
        #end of shopping     
        elif(flag=="3"):
            break
        else:
            flag=input("To add a product click 1,for Deleting a product click 2, to cart click 3:  ")
if __name__=='__main__':
    main()
