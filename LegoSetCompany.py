#main class for menu processing
import OnlineOperations
from Store import Store
online = OnlineOperations.OnlineOperations()

def print_main_menu():
    option = 't'
    while not (option == 'i' or option =='o' or option == 'x'):
        print("Main Menu\n (o)nline orders\n (i)n store orders\n e(x)it")
        option = input("what do you choose?: ")
        option = option.lower()
    return option

def print_online_menu():
    online.login()
    option = ''
    while not (option == 'x'):
        print("Online Menu\n (s)earch bricks\n (b)uy bricks\n (e)dit profile\n e(x)it")
        option = input("what do you choose?: ")
        option = option.lower()

        if option == 's':
            online.search_bricks()
        elif option =='b':
            online.buy_bricks()
        elif option =='e':
            online.edit_profile()
        else:
            print("invalid option")
        

def print_in_store_menu():
    run = Store()
    run.inStoreMenu()

option = 't'
while not option.lower() == 'x':
    option = print_main_menu()
    if option == 'o':
        print_online_menu()
    elif option == 'i':
        print_in_store_menu()
    else:
        print("invalid option")


#create menu
