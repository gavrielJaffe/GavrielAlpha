class Costumer:
    def __init__(self,costumer_name):
        self.costumer_name=costumer_name
        self.all_products={}
        self.Total_purchase_amount=0
                     
    def AddProduct(self):
        #get product name,price,quantity. 
        product_name=input("enter name of product:")
        price=input("enter price of product: ") 
        while not(price.isdigit()):
            price=input("enter price of product: ")
        price=int(price)
        quantity=input("enter quantity number to purchase:")
        while not( quantity.isdigit()):
            quantity=input("enter quantity number to purchase: ")
        quantity=int(quantity)
        if(product_name in self.all_products):
            self.all_products[product_name]["unit_number"]=self.all_products[product_name]["unit_number"]+ quantity
            print("all_products",self.all_products) 
            
        else:
            self.all_products[product_name]={"price_product":price,"unit_number":quantity}
            print("all_products",self.all_products)
            #we need to go all over the 
        self.Total_purchase_amount+=(price*quantity)            
    def RemoveProduct(self):
        prodact_remove = input("enter the product you want to remove?\n")
        product_quantity_remove = input("how many item you want to remove from it?\n")
        if(self.all_products=={}):
            if(prodact_remove in self.all_products):
                product_quantity_remove =int(product_quantity_remove)
                if(product_quantity_remove<0):
                    print("you enter invalid number")
                elif(product_quantity_remove >= self.all_products[prodact_remove]["unit_number"]):
                     del self.all_products[prodact_remove]
                     print(self.all_products)
                else:
                    self.all_products[prodact_remove]["unit_number"] =self.all_products[prodact_remove]["unit_number"]- product_quantity_remove
                    print(self.all_products)
        else:
            self.all_products[prodact_remove]["unit_number"]=self.all_products[prodact_remove]["unit_number"]-product_quantity_remove
            print(self.all_products)

                 
