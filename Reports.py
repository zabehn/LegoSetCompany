from Database import Database

class Reports(object):
    """all the different reports compiled"""
    def _init_(self):
        self.database = Database()

    def print_menu(self):
        print("Reports\n (D)aily Sales\n (W)eekly Sales\n (P)urchases by Employees\n Sales by (E)mployee\n Purchases by (C)ustomer\n E(x)it")
        option = 't'
        while not option == 'x':
            option = input("what would you like to pick?: ")
            option = option.lower()
            if option == 'd':
                daily_sales_reports()
            elif option == 'w':
                weekly_sales_reports()
            elif option == 'e':
                sales_by_employee()
            elif option == 'c':
                purchases_by_customer()
            elif option =='p':
                purchases_by_employee()
            else:
                print("invalid option")

    def daily_sales_reports(self):
        print("Daily Sales Reports")
        mycursor = self.database.cursor

    def weekly_sales_reports(self):
        print("Weekly Sales Reports")

    def purchases_by_employee(self):
        employee = input("what employee do you want to see purchases from (id): ")
        print("Purchases by " + employee)
        query = 'Select Order.Order_Id,Order.Price from Stock_Order right join Order on order.order_id = Stock_Order.Order_Order_ID where Stock_Order.employee_id = ' + employee
        mycursor = self.database.cursor
        mycursor.execute(query)
        for row in mycursor:
            print("order_id: "+row[0] +", Price: $"+row[1])

    def sales_by_employee(self):
        employee = input("what employee do you want to see purchases from (id): ")
        query = 'Select Order.Order_Id,Order.Price from In_Store_Order right join Order on order.order_id = in_store_order.Order_Order_ID where in_store_order.employee_id = ' + employee
        mycursor = self.database.cursor
        mycursor.execute(query)
        print("Sales by: "+employee)
        for row in mycursor:
            print("order_id: "+row[0] +", Price: $"+row[1])
        

    def purchases_by_customer(self):
        customer = input("what customer do you want to see purchases from (id): ")
        print("Purchases by: " + customer)
        query = 'Select Order.Order_Id,Order.Price from Online_Order right join Order on order.order_id = Online_Order.Order_Order_ID where Online_Order.Customer_ID = ' + customer
        mycursor = self.database.cursor
        mycursor.execute(query)
        print("Purchases by: "+customer)
        for row in mycursor:
            print("order_id: "+row[0] +", Price: $"+row[1])