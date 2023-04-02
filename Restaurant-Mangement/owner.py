import items, orders

def update():
    while True:
        print("\n\n******** MENU *********")
        print("\n1. -- Add an Item --")
        print("2. -- Delete an Item --")
        print("3. -- Update Price of an Item --")
        print("4. -- Go Back To Previous Menu --\n")
        ch = int(input(" -->> Your Choice :- "))
        if ch == 1:
            items.add()
        elif ch == 2:
            items.delete()
        elif ch == 3:
            items.update()
        elif ch == 4:
            break
        else:
            print("\nWrong Choice !! Please enter Correct Choice --")
            ch = int(input(" -->> Your Choice :- "))

def task():
    while True:
        print("\n{}\n{}{}{}\n{}\n".format("-"*64," "*26,"THINGS TO DO"," "*26,"-"*64))
        print("\n1. Update Items List.")
        print("2. Dispatch Orders.")
        print("3. View Items List.")
        print("4. Close.")
        print("\n{}".format("-"*64))
        ch = int(input("--->> Enter Your Choice :- "))
        if ch == 1:
            update()
        elif ch == 2:
            orders.dispatch()
        elif ch == 3:
            items.itemslist()
        elif ch == 4:
            return
        else:
            print("\n......Wrong Choice Entered......")
