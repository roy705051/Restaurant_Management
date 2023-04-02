from functions import ischeck, iscontain, isvalid
import items,pwinput

def customer():
    c = Customer()
    print("\n","*"*42,">> CUSTOMER PAGE <<","*"*42,"\n")
    print("\nPress 1 to Sign UP (New Customer).\nPress Any other Number to Login (Existing Customer)")
    ch = int(input("\nYour Choice -->> "))
    if ch == 1:
        c.new_user()
    else:
        c.ext_user()
    
class Customer:
    def __init__(self):
        self.user_n = None
        self.pass_w = None
    
    def new_user(self):
        print("\n","-"*32,">> SIGN UP PAGE <<","-"*32)
        self.user_n = input("\nEnter a Unique User Name -->> ")
        while iscontain(self.user_n):
            print("\nUser Name Already Taken !!!")
            self.user_n = input("\nEnter a Unique User Name -->> ")

        self.pass_w = pwinput.pwinput("Enter PassWord -->> ")
        while isvalid(self.pass_w) == False:
            print("\nNote :- Password must be 6 characters long, at least 1 Upper and lower case, 1 digit and 1 special character.")
            self.pass_w = pwinput.pwinput("Enter a Valid Password -->> ")

        with open("customers.txt","a") as flp:
            text = " ".join([self.user_n, self.pass_w]) + '\n'
            flp.writelines(text)
        print("User Successfully registered :)")
        items.itemslist()
        items.take_Orders()

    def ext_user(self):
        print("\n","-"*32,">> LOGIN PAGE <<","-"*32)
        self.user_n = input("\nEnter User Name -->> ")
        self.pass_w = pwinput.pwinput(prompt="Enter PassWord -->> ")
        if iscontain(self.user_n) == False:
            print("User Not Registered !! Please Register Yourself")
            self.new_user()
            return
        while ischeck(self.user_n, self.pass_w) == False:
            print("\nIncorrect Password !!")
            self.pass_w = pwinput.pwinput(prompt="Enter Correct Password -->> ")
        print("\nLogged in SuccessFully :)")
        items.itemslist()
        items.take_Orders()