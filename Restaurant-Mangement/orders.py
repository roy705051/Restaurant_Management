import time
def orderlist():
    print("\n\n{} >> ORDER LIST << {}\n".format("-"*23,"-"*23))
    with open("orderslist.txt","r") as ol:
        data = ol.readlines()
        if len(data)==0:
            return -1234
        for i in data:
            arr = i.strip().split(',')
            print("Order No. {} ---> {}".format(arr[0],arr[1]))
        print()

def dispatch():
    if orderlist()==-1234:
         print("No Orders Available To Dispatch !!")
    else:
        ord_l = input("Enter Order Nos. To Dispatch ---> ").split()
        for i in ord_l:
            temp_l = []
            with open("orderslist.txt","r") as ol:
                data = ol.readlines()
                for j in data:
                    arr = j.strip().split(',')
                    if arr[0] == i:
                        continue
                    ux = ",".join(arr)+"\n"
                    temp_l.append(ux)
            open("orderslist.txt","w").close()
            with open("orderslist.txt","w") as ol:
                for k in temp_l:
                    ol.writelines(k)
        print()
        print("\nDispatching Orders ....\n")
        for i in ord_l:
            time.sleep(2)
            print("Order No. {} Dispatched Succesfully.".format(i))
        print("\nAll Orders Dispatched Successfully ......\n")        