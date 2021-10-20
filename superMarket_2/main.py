from Costumer import Costumer
from Register import Register
    
all_costumers={}
def main():
    register_list_obj=[]
    end_of_shooping=2
    diffrent_register='9'
    while(end_of_shooping!='5'):
        if(diffrent_register =='9'):
            new_register=Register()
            register_list_obj.append(new_register)
        user_action=4
        costumer_name=input("Hello,enter your name: \n")
        new_costumer=Costumer(costumer_name)
        #new_register.prints_summary(new_costumer)
        while(user_action!="3"):
            user_action=input("To add a product click 1,Deleting a product click 2, to cart click 3:")   
            if(user_action=="1"):
                new_costumer.add_product()
            elif(user_action=="2"):
                new_costumer.remove_product()
            elif(user_action=="3"):
                new_register.check_out_customer(new_costumer)
                new_register.prints_summary(new_costumer)
                print("done")
                end_of_shooping=input("to End of shooping press 5,otherwis press any key.")
                if (end_of_shooping!='5'):
                    diffrent_register=input("to go to a new Register prees 9,otherwis press any key.")
           # to get the biges dictionary with:  name ,product ,price,quantity.
            print("new_register.overall_sales_list: ",new_register.overall_sales_list)
            #print the dic in nice way.
            for p_id, p_info in new_register.overall_sales_list.items():
                print("\n Person name: ", p_id)
                for key in p_info:
                    print(key + ':', p_info[key])
            #print the sum of register's
            for i in register_list_obj:                
                print("main 40",i.overall_sales_list)



if(__name__=="__main__"):
   main()