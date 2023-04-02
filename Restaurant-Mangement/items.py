from random import randint as rd
from functions import isAvailabe_Price

def getItem(num):
    with open("items.txt","r") as it:
        data = it.readlines()
        for i in data:
            arr = i.strip().split(', ')
            if int(arr[0]) == num:
                return arr[1]

def itemslist():
    print("\n\n{} >> ITEM LIST << {}\n".format("-"*24,"-"*23))
    with open("items.txt", "r") as it:
        data = it.readlines()
        for i in data:
            t_arr = i.split(',')
            print("{}. {} -->> Rs.{}".format(t_arr[0],t_arr[1],t_arr[2]))

def take_Orders():
    print("\n{}\n{}{}{}\n{}\n".format("-"*64," "*24,"Place Your Order"," "*24,"-"*64))
    ch = "y"
    total_price = 0
    ord_no = rd(100,500)+rd(100,300)+rd(100,200)
    i_arr = [str(ord_no)]
    while ch == "y":
        num = int(input("Choose Dish Number -->> "))
        if isAvailabe_Price(num) == -1:
            print("Incorrect Dish Number !!! Please Choose Correct Dish Number !!!\n")
            continue
        qty = int(input("Enter Quantity    -->> "))
        item_p = isAvailabe_Price(num)
        total_price += item_p * qty
        item_name = getItem(num)
        print(item_name)
        toadd = " ".join([item_name,str(qty)])
        i_arr.append(toadd)
        ch = input('\nHit "y" to Choose Another Dish -->> ')
    
    with open("orderslist.txt","a") as ord_list:
        info = ",".join(i_arr)+'\n'
        ord_list.writelines(info)
    
    #Display Order
    k=1
    print("\n\n------------------>> Your Order <<------------------\n")
    print("-->> Order Number :- ",ord_no)
    print("\n-->> Items :- \n")
    for i in range(1,len(i_arr)):
        print("{}. {}".format(k,i_arr[i].strip()))
        k+=1
    print("\n------------->> Total Price:- Rs. {} <<--------------".format(total_price))
    ch = input('\nHit "y" to Confirm Order = ')
    if ch == "y":
        print("\nOrder Has Been Placed !!\n")
    else:
        print("\nOrder Has Been Cancelled !!\n")

def add():
    ch = "y"
    with open("items.txt", "r") as f:
        data = f.readlines()
        arr = data[-1].strip().split(',')
        num = int(arr[0])
    while ch == "y":
        i_name = input("Enter Item Name -->> ")
        i_price = input("Enter Item Price -->> ")
        i_num = str(num+1)
        toadd = [i_num,i_name,i_price]
        with open("items.txt","a") as flp:
            flp.writelines(", ".join(toadd)+"\n")
        ch = input('\nHit "y" to continue (y/n) : ')
    print("\n -- Items List Successfully Updated !! --")

def delete():
    itemslist()
    ch = "y"
    flag = True
    while ch == "y" and flag:
        num = input("\nEnter Item Number To Remove :- ")
        if isAvailabe_Price(int(num)) == -1:
            print("\nItem Not Found !! Please Enter Valid Item Number -- ")
            continue
        k = 1
        with open("items.txt", "r") as f:
            data = f.readlines()
            temp_d = []
            for i in data:
                arr = i.strip().split(",")
                if num == arr[0]:
                    continue
                else:
                    arr[0] = str(k)
                    ux = ",".join(arr)+"\n"
                    temp_d.append(ux)
                    k += 1
        open("items.txt","w").close()
        with open("items.txt","a") as f:
            for i in temp_d:
                f.writelines(i)
        print("\n -- Item No. {} Successfully Deleted !! --".format(num))
        ch = input('\nHit "y" to continue (y/n) : ')
        itemslist()
        with open("items.txt","r") as f:
            data = f.readlines()
            if len(data) == 0:
                print("\n -- Empty Item List -- ")
                flag = False
    
def update():
    ch = "y"
    itemslist()
    while ch == "y":
        num = input("\nEnter Item Number :- ")
        if isAvailabe_Price(int(num)) == -1:
            print("\nItem Not Found !! Please Enter Valid Item Number -- ")
            continue
        price = input("Enter the Updated Price :- ")
        temp_d = []
        with open("items.txt", "r") as f:
            data = f.readlines()
            for i in data:
                arr = i.strip().split(',')
                if arr[0] == num:
                    arr[2] = price
                ux = ",".join(arr)+"\n"
                temp_d.append(ux)
                    
        open("items.txt","w").close()
        with open("items.txt","a") as f:
            for i in temp_d:
                f.writelines(i)
        print("\n -- Price SuccessFully Updated --")
        itemslist()
        ch = input('\nHit "y" to continue (y/n) : ')


    