"""
Scrieti o aplicatie care are interfata utilizator tip consolă cu un meniu:
1 Citirea unei liste de numere intregi
2, 3, 4 Gasirea secventelor de lungime maxima care respectă o proprietatea dată:
    - 2. Contine cel mult trei valori distincte
    - 6. sunt toate distincte intre ele
    - 8. au toate elementele in [0, 10]
0 Iesire din aplicatie.
Documentatia să contină:
 Scenarii de rulare pentru cele două cerinte primite (vezi curs 1 – scenarii de rulare)
 Cazuri de testare pentru cele doua cerinte în format tabelar (vezi curs 1 – cazuri de testare)
"""
#Functionality

#nicely print a list
def print_list(lista:list[int]):
    """
    afiseaza lista pe aceeasi linie cu spatiu intre elemente
    :param list: lista ce dorim sa fie afisata; preconditie: lista de tipul [1, 2, 3]
    :return: no return
    """
    for i in lista:
        print(i, end=" ")
    print()

#menu option 1
def read_list()->list[int]:
    """
    Citeste o lista cu n elemente, unde si n este citit
    :return: lista citita
    """
    lista_citita = []
    n = -1
    while True:
        try:
            n = int(input("Cate elemente are lista?\n"))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Introdu un numar mai mare ca 0")
    for i in range(n):
        print(f"Introdu numarul cu pozitia {i}:")
        ok = False
        while not ok:
            try:
                lista_citita.append(int(input("Nr:")))
                ok = True
            except ValueError:
                print("Informatia introdusa nu este valida")

    return lista_citita

#menu option 2
def cel_mult_trei_valori_distincte_subsecventa(lista:list[int], index: int)->list[int]:
    """
    Gaseste subsecventa (continua) de lungime maxima cu cel mult 3 valori distincte incepand cu un index a carei valoare este inclusa
    :param lista: lista unde dorim sa gasim subsecventa; preconditie : lista de tipul [1, 2, 3]
    :param index: indexul de unde se doreste ca subsecventa sa inceapa
    :return: subsecventa gasita
    """
    numbers = set()
    sequence = []
    for i in range(index, len(lista)):
        if(len(numbers) != 3):
            sequence.append(lista[i])
            numbers.add(lista[i])
        elif not lista[i] in numbers:
            break
    return sequence

def cel_mult_trei_valori_distincte_toata_lista(lista:list[int])->list[int]:
    """
    Gaseste subsecventa (continua) de lungime maxima de cel mult 3 valori distincte dintr-o lista
    :param lista: lista unde dorim sa cautam subsecventa; preconditie: lista de tipul [1, 2, 3]
    :return: subsecventa gasita
    """
    list_to_return = []
    for i in range(0, len(lista)):
        temp = cel_mult_trei_valori_distincte_subsecventa(lista, i)
        if(len(temp) > len(list_to_return)):
            list_to_return = temp[:]
    return list_to_return

#menu option 3
def toate_distincte_subsecventa(lista:list[int], index:int)->list[int]:
    """
    Gaseste subsecventa (continua) de lungime maxima unde toate elementele dintr-o lista sunt distincte intre ele, incepand cu un index care este inclus in subsecventa cautata
    :param lista: lista unde dorim sa cautam subsecventa
    :param index: indexul de unde se doreste a se incepe cautarea
    :return: subsecventa maxima gasita
    """
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
    """
    Gaseste subsecventa (continua) de lungime maxima din lista unde toate elementele sunt distincte intre ele
    :param lista: lista unde dorim sa cautam aceasta subsecventa
    :return: subsecventa gasita
    """
    result = []
    for i in range(len(lista)):
        temp = toate_distincte_subsecventa(lista, i)
        if(len(temp) > len(result)):
            result = temp[:]
    return result

#menu option 4
def subsecventa_nr_cuprinse_0_10_starting_index(lista:list[int], index:int)->list[int]:
    """
    Gaseste subsecventa (continua) de lungime maxima unde toate elementele sunt cuprinse in [0,10] pornind de la un index dat care este inclus in lista finala daca satisface conditia
    :param lista: lista unde dorim sa cautam subsecventa
    :param index: indexul de unde dorim sa incepem cautarea in lista data
    :return: subsecventa maxima gasita
    """
    end = index
    while (end < len(lista) and lista[end] >= 0 and lista[end] <= 10):
        end += 1
    return lista[index:end]

def subsecventa_nr_cuprinse_0_10_toata_lista(lista:list[int])->list[int]:
    """
    Gaseste subsecventa (continua) de lungime maxima din intreaga lista unde toate elementele sunt cuprinse in [0, 10]
    :param lista: lista unde dorim sa cautam subsecventa
    :return: subsecventa maxima gasita
    """
    return_list = [];
    for i in range(len(lista)):
        temp = subsecventa_nr_cuprinse_0_10_starting_index(lista, i)
        if(len(temp) > len(return_list)):
            return_list = temp[:]
    return return_list


#middleware
def middleware_functions_list(ok_list:bool)->bool:
    """
    Verifica pentru fiecare apel care depinde de lista daca aceasta a fost sau nu citita
    :param ok_list: valoare care atesta sau nu ca o lista a fost citita
    :return: valoare care permite sau nu efectuarea operatiilor pe baza listei
    """
    if not ok_list:
        print("Mai intai citeste o lista")
        return False
    return True


#-------------------
#menu interact
def menu_interact() -> int:
    """
    Interactionarea cu meniul - citire de valori pentru a interaction cu meniul
    :return: valoarea citita
    """
    while True:
        try:
            x = int(input("Introdu optiunea pe care doresti sa o urmezi: \n"))
            if(x < 0 or x > 4):
                raise ValueError
            return x
        except ValueError:
            print("Introdu o valoare valida")

def menu_print():
    """
    Afiseaza meniul pe care il avem disponibil pentru a utiliza functionalitatile aplicatiei
    :return:
    """
    print("Alege una dintre urmatoarele optiuni prin introducerea ID-ului asociat fiecareia")
    print("1 - Citirea unei liste de numere intregi")
    print("2 - Gasirea secventei de lungime maxima care contine cel mult trei valori distincte")
    print("3 - Gasirea secventei de lungime maxima care sunt toate distincte intre ele")
    print("4 - Gasirea secventei de lungime maxima care are toate elementele in [0,10]")
    print("0 - Iesi din aplicatie")
#----------------------


def main():
    """
    Functia principala care trebuie apelata pentru a rula programul
    :return:
    """
    menu_option = -1
    list_main = []
    ok_lista = False
    while(menu_option != 0):
        menu_print()
        menu_option = menu_interact()
        if(menu_option == 1):
            list_main = read_list()[:]
            print("Lista citita este: ")
            print_list(list_main)
            ok_lista = True
        elif(menu_option==2):
            if middleware_functions_list(ok_lista):
                print("Secventa de lungime maxima care contine cel mult 3 valori distincte este: ")
                print_list(cel_mult_trei_valori_distincte_toata_lista(list_main))
        elif(menu_option==3):
            if middleware_functions_list(ok_lista):
                print("Secventa de lungime maxima in care toate elementele sunt distincte intre ele este: ")
                print_list(toate_distincte_toata_lista(list_main))
        elif(menu_option==4):
            if middleware_functions_list(ok_lista):
                print("Secventa de lungime maxima in care toate elementele sunt in intervalul [0,10] este:")
                print_list(subsecventa_nr_cuprinse_0_10_toata_lista(list_main))
    print("bye bye")

main()