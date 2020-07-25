from Customer import Customer
import Order

class OnlineOperations(object):
    """all online customer operations"""
    def _init_(self):
        self.order = Order()
        self.customer = Customer()

    def username_exists(name):
        #search database for username, return true if found
        if not name == name:
            return True;
        return False;

    def search_for_username(): 
        name = input("Username: ")
        while not username_exists(name) or not username.lower() == "x":
            username = input("Username doesn't exist \nUsername: \nTo create an account enter (x)")
            #probe database for username

        #create customer from data
        return Customer()

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
            OnlineOperations.query_bricks(description=temp)
        elif option == 's':
            temp = input("what Set ID would you like to search?: ")
            OnlineOperations.query_bricks(set_id=temp)
        elif option == 'p':
            temp = input("what Product ID would you like to search?: ")
            OnlineOperations.query_bricks(product_id=temp)
        else:
            print("invalid option")
    
    def query_bricks(description = None,set_id = None, product_id = None):
        if not description == None:
            print("Legos with: " + description + " in description")
            #query database based on description
        elif not set_id == None:
            print("Legos with: " + set_id + " in description")
            #query database based on set_id
        elif not product_id == None:
            print("Legos with: " + product_id + " in description")
            #query database based on product_id

    def buy_bricks(self):
        option = ''
        while not (option == 's' or option == 'p'):
            option = input("buy bricks by set (s) or product (p) ID?")
            option.lower()

        if option == 'p':
            print("this is the brick you selected:\n")
            #query database based on product id
        elif option == 's':
            print("these are the bricks in the set you selected:\n")
            #query the database based on set id

        while not (option == 'y' or option == 'n'):
            option = input("is this the brick(s) you want? (y/n)")
            option.lower()
        if(option == 'y'):
            print("added to order")
            #for items in query add to the order
            self.order.add_to_order(1,1)
        elif option == 'n':
            print("not added to order")
        else:
            print("invalid option")
    
    def edit_profile(self):
        option = ''
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
