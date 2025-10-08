n = int(input("introdu nr n pentru a gasi nr minim format din aceleasi cifre"))
rasp = 0
nr = [0 for i in range(10)]

while n != 0:
    nr[n%10] += 1
    n //= 10

for i in range(10):
    for j in range(nr[i]):
        rasp = rasp * 10 + i

print(rasp)