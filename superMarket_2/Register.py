class Register:
    def __init__(self):
        self.profit_amount=0
        self.overall_sales_list={}

    def check_out_customer(self,costumer): 
        self.profit_amount+=costumer.price_in_cart
        self.overall_sales_list[costumer.costumer_name]=costumer.all_products

    def prints_summary(self,costumer):
        print("(line 11)over all in this Register:\n ",self.overall_sales_list)
        print("self.profit_amount",self.profit_amount)
        