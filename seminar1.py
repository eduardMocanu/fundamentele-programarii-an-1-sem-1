import math


def este_prim(x: int):
    if (x < 2):
        return False
    elif (x == 2):
        return True
    elif (x % 2 == 0):
        return False
    for d in range(3, int(math.sqrt(x)) + 1):
        if (x % d == 0):
            return False
    return True

def gasire_nr(x:int):
    index = x

    while (True):
        index += 1
        prim = este_prim(index)
        if (prim):
            return index

x = 0
while(x!=2):
    print("1.Gasirea celui mai mic nr prim")
    print("2.Exit")
    x = int(input())
    if(x==1):
        nr = int(input("Introdu un nr: "))
        print(gasire_nr(nr))
    else:
        x = 2



