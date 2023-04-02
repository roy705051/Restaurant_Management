import users,owner
import pwinput

def owner_login():
    _pass_w = "Rest@123" 
    pwd = pwinput.pwinput(prompt="---->> Enter Password :- ")
    while pwd != _pass_w:
        print("\nIncorrect Password !!!\n")
        pwd = pwinput.pwinput(prompt="---->> Enter Correct Password :- ")
        
    print("\n**************** LOGGED IN SUCCESSFULLY *******************\n")

print("\n","-"*52,">> \U0001F60B WELCOME TO PARADISE RESTAURANT \U0001F60B <<","-"*52)
print('\n1. Press 1 for Organisational User. \U0001F468')
print('2. Press 2 for Customer User. \U0001F9D1')
inp = int(input("\nYour Choice -->> "))
while inp != 1 and inp != 2:
    print("\nPlease Enter Correct Reference !!!")
    inp = int(input("Your Choice -->> "))
    
if inp == 1:
    owner_login()
    owner.task()
    print("\n\nExiting The Window ...............")
elif inp == 2:
    users.customer()
    print("\n{}>> THANK YOU VISIT AGAIN !! <<{}\n".format("-"*32,"-"*32))