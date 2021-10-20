class Costumer:
    def __init__(self,costumer_name):
        self.costumer_name=costumer_name
        self.all_products={}
        self.price_in_cart=0
                     
    def add_product(self):
        #get product name,price,quantity. 
        product_name=input("enter name of product:")
        price=input("enter price of product: ") 
        while not(price.isdigit()):
            price=input("enter price of product ")
        price=int(price)
        quantity=input("enter quantity number to purchase:")
        while not( quantity.isdigit()):
            quantity=input("enter quantity number to purchase: ")
        quantity=int(quantity)        
        if (product_name in self.all_products):
            self.price_in_cart +=quantity*self.all_products[product_name]["price_product"]     
            self.all_products[product_name]["unit_number"]=self.all_products[product_name]["unit_number"]+ quantity
            print("all_products line 21",self.all_products) 
        else:
            self.all_products[product_name]={"price_product":price,"unit_number":quantity}
            self.price_in_cart+=self.all_products[product_name]["unit_number"]*self.all_products[product_name]["price_product"]
            print("all_products",self.all_products)
        # gives us price in cart.  
        print("price in cart line 28",self.price_in_cart)
    def remove_product(self):
        if(self.all_products=={}):
            print("no product in your cart")
        else:
            product_remove = input("enter the product you want to remove?\n")
            if(product_remove in self.all_products):
                product_quantity_remove = input("how meany item you want to remove from it?\n")
                product_quantity_remove =int(product_quantity_remove)
                if(product_quantity_remove<0):
                    print("you enter invalid number")
                elif(product_quantity_remove >= self.all_products[product_remove]["unit_number"]):
                     self.price_in_cart-= self.all_products[product_remove]["unit_number"]*self.all_products[product_remove]["price_product"]
                     del self.all_products[product_remove]
                     print(self.all_products)
                     print("price is cart : ",self.price_in_cart)
                else:
                    self.all_products[product_remove]["unit_number"] = self.all_products[product_remove]["unit_number"]- product_quantity_remove
                    price_in_cart=self.price_in_cart-product_quantity_remove*self.all_products[product_remove]["price_product"]
                    print(self.all_products)
                    print("price is cart : ",price_in_cart)
            else:
                print("price is cart : ",self.price_in_cart)     
                print("item no in cart") 
                         

                 
