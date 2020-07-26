from Database import Database

class Store(object):
    def __init__(self, employeeId=None, employeePasswd=0):
        self.employeeId = employeeId
        self.employeePasswd = employeePasswd

        self.database = Database()
    
    def inStore(self):
        self.employeeId = int(input("EMPLOYEE ID:"))
        self.employeePasswd = input("PASSWORD:")

        query = "Select * FROM Employee"
        mycursor = self.database.cursor
        mycursor.execute(query)

        for row in mycursor:
            while row[0] == self.employeeId and row[1] == self.employeePasswd:
                self.inStoreMenu()
                pick = input("Pick from above: ")
                if int(pick) == 1:
                    self.takeOrder()
                elif int(pick) == 2:
                    self.employeeManagement()
                elif int(pick) == 3:
                    pass
                elif int(pick) == 4:
                    self.storeManagement()
                elif int(pick) == 5:
                    pass
                elif int(pick) == 6:
                    self.changePassword()
                elif int(pick) == 0:
                    print("Goodbye")
                    break
                else:
                    print("Invalid!")
                    break
    
    def takeOrder(self):
        query = "select * from products"
        mycursor = self.database.cursor
        mycursor.execute(query)

        while True:
            print("------------------------------\n1: Set \n2: Product\n0: Exit")
            pick = input("Option: ")
            if int(pick) == 1:

                setId = input("Enter Set ID:")
                sDescription = ""
                for row in mycursor:
                    if row[3] == int(setId):
                        sDescription = "".join("You Have Selected a Set : " + row[2])
                print(sDescription)
            elif int(pick) == 2:

                productId = input("Enter Product ID:")
                pDescription = ""

                query1 = "Select * from Store_has_Products"
                mycursor1 = self.database.cursor
                mycursor1.execute(query1)

                nProducts = input("Number of Products: ")

                for row in mycursor:
                    if row[0] == int(productId):
                        pDescription = "".join("You Have Selected a Product: " + row[2])

                        for info in mycursor1:
                            if int(productId) == info[1] and int(nProducts) < info[2]:
                                print(pDescription, "\nQuantity: ", nProducts)
                                self.acceptPayment()

                            else:
                                break


            elif int(pick) == 0:
                print("Exiting....")
                break
            else:
                print("Invalid")

    def acceptPayment(self):
        print("-----------Payment------------\n1: Cash\n2: Card")
        payment = input("Option: ")
        if int(payment) == 1:
            pass
        elif int(payment) == 2:
            cardNum = input("Enter Card Number: ")
            bAddress = input("Billing Address: ")
            cType = input("Card Type(AMEX, MC, Visa, etc.): ")
            cardInfo = (cardNum, bAddress, cType)
            query = "INSERT INTO Payment(Card_Num,Billing_Address,Card_Type)VALUES(%s,%s,%s) "
            mycursor = self.database.cursor
            mycursor.execute(query, cardInfo)
            self.database.cnxncommit()

            """
            query = "select * from products"
            mycursor = self.mydb.cursor()
            mycursor.execute(query)

            for productinfo in mycursor:
                if productinfo[0] == self.takeOrder().productId:
                    inStoreInfo = ("Card", productinfo[4], self.employeeId, cardNum)
                    query2 = "INSERT INTO instoreorder(Pay_MethodPayment, Order_Order_ID, " \
                             "Employee_Employee_ID,Payment_Card_Num)VALUES(%s,%s,%s,%s) "
                    mycursor2 = self.mydb.cursor()
                    mycursor2.execute(query, inStoreInfo)
                    self.mydb.commit()
            """



        else:
            pass

    def employeeManagement(self):
        while True:
            print("----------Employee Management-----------\n1: List Employees\n2: Add Employee\n0: Exit")
            pick = input("Option: ")
            if int(pick) == 1:
                query = "Select * FROM Employee"
                mycursor = self.database.cursor
                mycursor.execute(query)

                print("\n------------------EMPLOYEE------------------\n\nEID\t\tNAME\t\tPOSITION")
                for row in mycursor:
                    # print(row[0], row[3], row[4])
                    first = str(row[0])
                    sec = str(row[3])
                    third = str(row[4])
                    print(first + "\t\t", sec + "\t\t", third)

                query = "Select * FROM Employee"
                mycursor = self.database.cursor
                mycursor.execute(query)
                print("\n---------------------------------------------")
                print("1: Select Employee\n2: Exit")
                pick = input("Option: ")
                if int(pick) == 1:
                    allinfo = ""
                    employee = input("Enter Employee ID: ")
                    for info in mycursor:
                        if int(employee) == info[0]:
                            allinfo = "".join("\tName: " + info[3] + "\n\tEmployee ID: " + str(info[0]) + "")

                    print("--------------Employee Info------------------\n")
                    print(allinfo)
                    print("\n----------------------------------------------")
                elif int(pick) == 2:
                    print("Exiting...")
                else:
                    print("invalid")

            elif int(pick) == 2:
                query = "INSERT INTO Employee(Employee_ID,Password, Salary,Name,Position,Date_Of_Hire," \
                        "Store_Store_ID)VALUES(%s,%s,%s,%s,%s,%s,%s) "
                name = input("Enter Employee Name:")
                id = input("Create Id:")
                password = input("Create Password:")
                salary = input("Enter salary:")
                position = input("Position:")
                sDate = input("Start date(yyyy-mm-dd):")
                storeId = input("Enter Store Id:")

                update = [(id, password, salary, name, position, sDate, storeId)]

                mycursor = self.database.cursor
                mycursor.executemany(query, update)
                self.database.cnxn.commit()
                print("New Employee Added")
            elif int(pick) == 0:
                print("Exiting....")
                break
            else:
                print("Invalid")

    def placeOrder(self):
        pass

    def storeManagement(self):
        query = "Select * From Store"
        mycursor = self.database.cursor
        mycursor.execute(query)

        count = 0
        print("-------------Stores-------------------")
        print("\tStore ID\tAddress")
        for row in mycursor:
            count += 1
            allinfo = "".join(str(count) + "\t" + str(row[0]) + "\t\t" + row[1])
            print(allinfo)
        print("---------------------------------")
        # add,delete and exit cases
        print("A or a:\tAdd Store\nD or d:\tDelete Store\nE or e:\tEdit/Update Address\n0:\tExit")
        while True:
            pick = input("Option: ")
            if pick == "A" or pick == "a":
                storeId = int(input("Enter Store ID: "))
                Address = input("Enter Address: ")
                info = (storeId, Address)

                query1 = "Insert into Store(Store_ID,Address)Values(%s,%s)"
                mycursor1 = self.database.cursor
                mycursor1.execute(query1, info)
                self.database.cnxn.commit()
                print("New Store Updated")
            elif pick == "D" or pick == "d":
                storeId = int(input("Enter Store ID: "))

                query2 = "select * from Store"
                mycursor2 = self.database.cursor
                mycursor2.execute(query2)
                self.database.cnxn.commit()

                for row1 in mycursor2:
                    if row1[0] == storeId:
                        query3 = "DELETE FROM Store WHERE Store_ID = %s"
                        mycursor3 = self.database.cursor
                        mycursor3.execute(query3, storeId)
                        self.database.cnxn.commit()
                        print("Store Removed")
                    else:
                        print("Sorry, Invalid Store ID")
            elif pick == "E" or pick == "e":
                storeId = input("Enter Store ID to Update the Address: ")
                newAddress = input("Enter New Address: ")
                args = (storeId, newAddress)
                query4 = "Update from Store WHERE Store_ID= %s and Address = %s "
                mycursor4 = self.database.cursor
                mycursor4.execute(query4, args)
                self.database.cnxn.commit()
                print("Address Updated")
            elif pick == "0":
                break
            else:
                print("invalid, please try again\n---------------------------------")

    def reports(self):
        pass

    def changePassword(self):
        newpassword = input("Enter New password:")
        query = "UPDATE Employee SET Password = %s Where Employee_ID = %s"
        args = (newpassword, self.employeeId)
        mycursor = self.database.cursor
        mycursor.execute(query, args)
        self.database.cnxn.commit()
        print("Password Updated")

    def inStoreMenu(self):
        print("\nEmployee#", self.employeeId, "\n")
        print("IN-STORE\n1.TAKE ORDER\n2.EMPLOYEE MANAGEMENT\n3.PLACE ORDER\n4.STORE "
              "MANAGEMENT\n5.REPORTS\n6.CHANGE PASSWORD\n0.Exit")

    def selectEmployee(self):
        query = "Select * FROM Employee"
        mycursor = self.database.cursor
        mycursor.execute(query)


