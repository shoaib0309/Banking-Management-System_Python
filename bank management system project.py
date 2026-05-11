
import random

class Account:
    def __init__(self, account_number, account_holder, __balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = __balance

          
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print (f"Amount {amount} successfully deposit")
            print (f"The current balance is {self.__balance}")
        else:
            print("Please, Enter valid amount above 0 rupees")

            
    def withDraw (self, amount):
        if amount <= 0:
            print ("Error! Invalid amount because your amount equel to 0 ")
            return

        if amount > self.__balance:
            print (f"you cannot withDraw amount ")
            return
        
        self.__balance -= amount
        print (f"Transaction successfully {amount} reduce from account")
        print (f"The current balance = {self.__balance}")
        return


    def display_balance (self):
        print (f" Account Holder: {self.account_holder} | Balance: {self.__balance} ")

    
class Bank:
    def __init__(self):
        self.accounts = {}


    def open_account (self):
        acc_number = random.randint(100000, 999999)

        if acc_number in self.accounts:
            print("Account is already found")
            return
        else:
            print ("Account does not found, Create new account")

        user_name = input("Enter User name:")
        card_No = int(input("Enter CNIC number:"))

        if len(str(card_No)) == 13:
            new_acc = Account(user_name, user_name, 0)
            self.accounts[acc_number] = new_acc
            print (" Congratulation!! Account succussfully opened")


            if len(str(acc_number)) == 6:
                print(f" your account number is: {acc_number}")

            else:
                print("Error! system generated invalid account number")

        else:
            print("invalid number! Enter 13 digits CNIC Number")


    def find_account(self, acc_number):
            
            if acc_number in self.accounts:
                print (f"{acc_number} is available")
                self.accounts[acc_number].display_balance()

            else:
                print(f"Account is not available")

bank_sys = Bank()
# Acc = Account()

while True:

    print("\t--- Liabrary Management System---")
    print(" 1:  Open Account ")
    print(" 2:  Deposit Balance")
    print(" 3:  WithDraw Balance")
    print(" 4:  Search Account ")
    print(" 5:  Display Balance ")
    print(" 6:  Exit ")

    user_choice = int(input("Enter the choice (1, 2, 3, 4, 5, 6): "))
    if user_choice not in [1, 2, 3, 4, 5, 6]:
        print ("invalid user choice")
        continue

    if user_choice == 1:
        bank_sys.open_account()

    elif user_choice == 2:
        acc_number = int(input("Enter Account Number for deposit: "))
        
        if acc_number in bank_sys.accounts:
            amount = int(input("Enter amount to deposit: "))
            bank_sys.accounts[acc_number].deposit(amount) 

        else:
            print("Error! Account Number not found.")



    elif user_choice == 3:
         acc_number = int(input("Enter Account Number for WithDraw: "))
        
         if acc_number in bank_sys.accounts:
            amount = int(input("Enter amount to withDraw: "))
            bank_sys.accounts[acc_number].withDraw(amount) 

         else:
            print("Error! Account Number not found.")


    elif user_choice == 4:
        acc_number = int(input("Enter Account Number for WithDraw: "))
        bank_sys.find_account(acc_number)


    elif user_choice == 5:
        acc_number = int(input("Enter Account Number for WithDraw: "))

        if acc_number in bank_sys.accounts:
            bank_sys.accounts[acc_number].display_balance() 

        else:
            print("Error! Account Number not found.")

                  

    elif user_choice == 6:
        break

    else:
        print ("you are enter wrong choice, Plz Enter valid choice")

        

            
            
        


        








            

        