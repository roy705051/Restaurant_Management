from string import ascii_uppercase as u, ascii_lowercase as l, digits as dgt, punctuation as p

def iscontain(name):
    with open("customers.txt", "r") as flp:
        data = flp.readlines()
        for i in data:
            arr = i.strip().split()
            if name == arr[0]:
                return True
        return False
    
def isvalid(pw):
    if len(pw) < 6:
        return False
    a,b,c,d = 0,0,0,0
    for i in set(pw):
        if i in u:
            a = 1
        elif i in l:
            b = 1
        elif i in dgt:
            c = 1
        elif i in p:
            d = 1
    if (a+b+c+d) < 4:
        return False
    else:
        return True

def ischeck(name, pw):
    with open("customers.txt", "r") as flp:
        data = flp.readlines()
        d = {}
        for i in data:
            arr = i.strip().split()
            d[arr[0]] = arr[1]
        if d[name] == pw:
            return True
        else:
            return False

def isAvailabe_Price(num):
    with open("items.txt","r") as fp:
        data = fp.readlines()
        for i in data:
            arr = i.strip().split(',')
            if int(arr[0]) == num:
                return int(arr[2])
        return -1