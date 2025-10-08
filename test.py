"""x = int(input("da un nr n pentru a putea iti da suma a n numere "))
s = 0
for i in range(x):
    s += int(input("Introdu in numar "))
print(f"suma este {s}")

import math

def prim(x:int):
    if(x < 2):
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False;
    return True

x = int(input("Introdu un nr pentru a vedea daca este prim"))
print(prim(x))

x = int(input("nr 1:"))
y = int(input("nr 2:"))

r = x % y
while(r != 0):
    x = y
    y = r
    r = x % y
print(y)

"""

