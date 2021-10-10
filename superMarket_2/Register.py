class Register:
    def __init__(self):
        self.profit_amount=0
        self.overall_sales_list={}

    def Check_out_Customer(self,costumer): 
        self.profit_amount+=costumer.Total_purchase_amount
        self.overall_sales_list[costumer.costumer_name]=costumer.Total_purchase_amount
    def PrintSummary(self,costumer):
        print("self.profit_amount",self.profit_amount)
        print("overall_sales_list:\n",self.overall_sales_list[costumer.costumer_name])