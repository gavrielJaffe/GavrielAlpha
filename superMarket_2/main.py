from Costumer import Costumer
from Register import Register
    
all_costumers={}
def main():
    user_action=4
    costumer_name=input("Hello,enter your name: \n")
    new_register=Register()
    new_costumer=Costumer(costumer_name)
    while(user_action!="3"):
        user_action=input("To add a product click 1,Deleting a product click 2, to cart click 3:")   
        if(user_action=="1"):
            new_costumer.add_product()
        elif(user_action=="2"):
            new_costumer.remove_product()
        elif(user_action=="3"):
            
            new_register.PrintSummary(new_costumer)
            
if(__name__=="__main__"):
   main()