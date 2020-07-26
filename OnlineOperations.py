from Customer import Customer
from Order import Order
from Database import Database

class OnlineOperations(object):
    """all online customer operations"""
    def _init_(self):
        self.database = Database()
        self.order = Order()
        self.customer = Customer()

    def username_exists(name):
        query = 'Select username from Customer'
        cursor = self.database.cursor
        for row in cursor:
            if row[0]==name:
                return True
        return False

    def search_for_username(self): 
        username = input("Username: ")
        while username_exists(username) or not username.lower() == "x":
            username = input("Username doesn't exist \nUsername: \nTo exit enter (x)")

        query = 'Select username,name,password,address From Customer WHERE username=' + username
        cursor = self.database.cursor
        cursor.execute(query)
        for row in cursor:
            return Customer(row[0],row[1],row[2],row[3])

    def get_address():
        zipcode = input("what is your Zip Code?: ")
        state = input("what is your state?: ")
        city = input("what is your city?: ")
        street = input("what is your street address?: ")
        return street + ', ' + city + ', ' + state + ', '+ zipcode

    def create_account():
        name = input("what is your name?: ")
        username = input("what is your username?: ")
        while OnlineOperations.username_exists(username):
            username = input("what is your username?: ")
        password = input("what is your password?: ")
        address = OnlineOperations.get_address()
        return Customer(name,username,password,address)

    def login(self):
        newAccount = input("Do you have an account? (Y/N)")
        if newAccount.lower() == 'n':
            self.customer = OnlineOperations.create_account()
            query = '''INSERT INTO Customer (username,password,address,name) VALUES(?, ?, ?, ?);'''
            values = (self.customer.username,self.customer.password,self.customer.address,self.customer.name)
            cursor = self.database.cursor
            cursor.execute(query,values)
            self.database.cnxn.commit()
        else:
            self.customer = search_for_username()
        password = input("Login\n what is your password?: ")
        while not self.customer.check_password(password):
            password = input("what is your password?: ")

    def search_bricks(self):
        option = ''
        while not option == 'x':
            option = input("what would you like to search by? \nDescription (d)\nSet_id (s)\nproduct_id(p)\ne(x)it: ")
            option = option.lower()

        if option == 'd':
            temp = input("what in the description would you like to search?: ")
            query_bricks(description=temp)
        elif option == 's':
            temp = input("what Set ID would you like to search?: ")
            query_bricks(set_id=temp)
        elif option == 'p':
            temp = input("what Product ID would you like to search?: ")
            query_bricks(product_id=temp)
        else:
            print("invalid option")
    
    def query_bricks(self, description = None,set_id = None, product_id = None):
        mycursor = self.database.cursor

        if not description == None:
            query = "select * from products where description like %" + description + "%"
            mycursor.execute(query)
            print("Legos with: " + description + " in description")
            for row in mycursor:
                print(" product id: " + row[0] + ", price: $"+row[1]+", set id: "+row[2] +", description: "+ row[3])
        elif not set_id == None:
            print("Legos with: " + set_id + " in set_id")
            query = "select * from products where set_id = " + set_id
            mycursor.execute(query)
            for row in mycursor:
                print(" product id: " + row[0] + ", price: $"+row[1]+", set id: "+row[2] +", description: "+ row[3])
        elif not product_id == None:
            print("Legos with: " + product_id + " in product_id")
            query = "select * from products where product_id = " + product_id
            mycursor.execute(query)
            for row in mycursor:
                print(" product id: " + row[0] + ", price: $"+row[1]+", set id: "+row[2] +", description: "+ row[3])

    def buy_bricks(self):
        option = 't'
        mycursor = self.database.cursor
        while not (option == 'x'):
            option = input("buy bricks by set (s) or product (p) ID?, (x) to finish ")
            option.lower()

            if option == 'p':
                print("this is the brick you selected:\n")
                query = "select * from products where product_id = " + product_id
                mycursor.execute(query)
                for row in mycursor:
                    print(" product id: " + row[0] + ", price: $"+row[1]+", set id: "+row[2] +", description: "+ row[3])
            elif option == 's':
                print("these are the bricks in the set you selected:\n")
                query = "select * from products where set_id = " + set_id
                mycursor.execute(query)
                for row in mycursor:
                    print(" product id: " + row[0] + ", price: $"+row[1]+", set id: "+row[2] +", description: "+ row[3])

            while not (option == 'y' or option == 'n'):
                option = input("is this the brick(s) you want? (y/n)")
                option.lower()
            if(option == 'y'):
                print("added to order")
                for row in mycursor:
                    self.order.add_to_order(row[0],1,row[1])
            elif option == 'n':
                print("not added to order")
            else:
                print("invalid option")
        
        query = 'Select Count(*) FROM Order'
        mycursor.execute(query)
        query = 'INSERT INTO ORDER (Order_ID,Price) VALUES(?,?);'
        for row in mycursor:
            i = row[0]
        mycursor.execute('Select Customer_ID from Customer where username = ' +self.customer.username)
        for row in mycursor:
            ci = row[0]
        values = (i,self.order.price)
        mycursor.execute(query,values)
        for x,y in zip(self.order.product_ids,self.order.product_quantities):
            query = "INSERT INTO ORDER_HAS_PRODUCTS (ORDER_ID, Product_ID) VALUES(?,?);"
            values = (i,x)
            mycursor.execute(query,values)
        payment = input("what is your card number?: ")
        card_type = input("what is your card type?: ")
        query = 'INSERT INTO PAYMENT (Card_Num, Billing_Address, card_type) VALUES(?,?,?);'
        values = (payment,self.customer.address,card_type)
        mycursor.execute(query,values)
        query = 'INSERT INTO CUSTOMER_ORDER (Payment_Card_Num,Customer_ID,Order_Id) VALUES(?,?,?);'
        values = (payment,ci,i)
        mycursor.execute(query,values)
        self.database.cnxn.commit()
    
    def edit_profile(self):
        option = 't'
        update_username = self.customer.username
        while not option == 'x':
            print(self.customer._str_())
            option = input("what would you like to change?\ntype (x) to exit: ")
            if option == 'n':
                self.customer.name = input("what is the new name?: ")
            elif option == 'p':
                self.customer.password = input("what is the new password?: ")
            elif option == 'u':
                username = input("what is the new username?: ")
                while not OnlineOperations.username_exists(username):
                    username = input("username is in use\nwhat is the new username?: ")
            elif option == 'a':
                self.customer.address = OnlineOperations.get_address()
            else:
                print("invalid option, try again")
        query = 'UPDATE Customer set Name = '+self.customer.name+ 'set password = '+ self.customer.password +'set username = '+self.customer.username+ 'set address = ' + self.customer.address + 'WHERE username = '+ update_username
        mycursor = self.database.cursor
        mycursor.execute(query)
        self.database.cnxn.commit()
