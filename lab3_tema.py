"""
Scrieti o aplicatie care are interfata utilizator tip consolă cu un meniu:
1 Citirea unei liste de numere intregi
2,3 Gasirea secventelor de lungime maxima care respectă o proprietatea dată:
    - Contine cel mult trei valori distincte
    - sunt toate distincte intre ele
4 Iesire din aplicatie.
Documentatia să contină:
 Scenarii de rulare pentru cele două cerinte primite (vezi curs 1 – scenarii de rulare)
 Cazuri de testare pentru cele doua cerinte în format tabelar (vezi curs 1 – cazuri de testare)



"""
#Functionality
#nicely print a list

def print_list(list:list[int]):
    for i in list:
        print(i, end=" ")

#menu option 1
def read_list()->list[int]:
    n = int(input("Cate elemente are lista?"))
    lista_citita = []
    for i in range(n):
        print(f"Introdu numarul cu pozitia {i}:")
        ok = False
        while(not ok):
            try:
                lista_citita.append(int(input("Nr:")))
                ok = True
            except ValueError:
                print("Informatia introdusa nu este valida")

    return lista_citita

#menu option 2
def cel_mult_trei_valori_distincte_subsecventa(lista:list[int], index: int)->list[int]:
    numbers = set()
    sequence = []
    for i in range(index, len(lista)):
        if(len(numbers) != 3):
            sequence.append(lista[i])
            numbers.add(lista[i])
        elif(not lista[i] in numbers):
            break
    return sequence

def cel_mult_trei_valori_distincte_toata_lista(lista:list[int])->list[int]:
    list_to_return = []
    for i in range(0, len(lista)):
        temp = cel_mult_trei_valori_distincte_subsecventa(lista, i)
        if(len(temp) > len(list_to_return)):
            list_to_return = temp[:]
    return list_to_return

#menu option 3
def toate_distincte_subsecventa(lista:list[int], index:int)->list[int]:
    list_to_return = []
    numbers = set()
    for i in range(index, len(lista)):
        if not lista[i] in numbers:
            list_to_return.append(lista[i])
            numbers.add(lista[i])
        else:
            break
    return list_to_return

def toate_distincte_toata_lista(lista:list[int])->list[int]:
    result = []
    for i in range(len(lista)):
        temp = toate_distincte_subsecventa(lista, i)
        if(len(temp) > len(result)):
            result = temp[:]
    return result


#-------------------
#menu interact
def menu_interact() -> int:
    x = int(input("Introdu optiunea pe care doresti sa o urmezi: \n"))
    while x > 4 or x <= 0:
        x = int(input("Introdu o optiune valida: \n"))
    return x

def menu_print():
    print("Alege una dintre urmatoarele optiuni prin introducerea ID-ului asociat fiecareia")
    print("1 - Citirea unei liste de numere intregi")
    print("2 - Gasirea secventelor de lungime maxima care contine cel mult trei valori distincte")
    print("3 - Gasirea secventelor de lungime maxima care sunt toate distincte intre ele")
    print("4 - Iesi din aplicatie")
#----------------------


def main():
    x = -1
    list_main = []
    ok_lista = False
    while(x != 4):
        menu_print()
        x = menu_interact()
        if(x == 1):
            list_main = read_list()[:]
            ok_lista = True
        elif(x==2):
            if(ok_lista):
                print_list(cel_mult_trei_valori_distincte_toata_lista(list_main))
            else:
                print("Mai intai trebuie sa citesti o lista")
        elif(x==3):
            if(ok_lista):
                print_list(toate_distincte_toata_lista(list_main))
            else:
                print("Mai intai trebuie sa citesti o lista")
    print("bye bye")

main()
#o scurta descriere pt fiecare functie cu ce face
#tipul parametrilor pe care ii accepta
#ce returneaza + tipul de return
#ce eroare raises si cand






