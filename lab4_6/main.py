"""
Cerințe generale:
• Folosiți procesul de dezvoltare: Incrementală bazată pe funcționalități (vezi
curs 1) și Dezvoltare dirijată de teste (curs 2)
• Planificați iterații pentru 3 laboratoare succesive. În fiecare săptămână primiți
o notă pentru ce s-a realizat pentru iterația din săptămâna curentă.
• Prima iterație trebuie sa conțină cel puțin 3 cerințe (din funcționalitățile 3-5)
• Documentația trebuie să conțină: enunțul, lista de funcționalități, planul de
iterații, scenarii de rulare, lista de taskuri (activități)
• Toate funcțiile trebuie să includă specificații, toate funcțiile trebuie sa fie
testate (funcții de test cu assert) în afară de partea cu interacțiunea utilizator.
• Separați partea de interfață utilizator de restul aplicației (sa nu aveți funcții
care fac 2 lucruri: un calcul + tipărire/citire)
• La prima iterație se cere o soluție procedurală (mai multe funcții toate în
același modul), varianta finală trebuie să fie modulară (curs 3)
• Datele de intrare trebuie validate, programul semnalează erorile către
utilizator.

lab 4 -
1. Adaugă număr în listă.
 • Adaugă număr complex la sfârșitul listei
 • Inserare număr complex pe o poziție dată.
2. Modifică elemente din listă.
 • Șterge element de pe o poziție dată.
 • Șterge elementele de pe un interval de poziții.
 • Înlocuiește toate aparițiile unui număr complex cu un alt număr
complex.
3. Căutare numere.
 • Tipărește partea imaginara pentru numerele din listă. Se dă intervalul
de poziții (sub secvența).
 • Tipărește toate numerele complexe care au modulul mai mic decât 10
 • Tipărește toate numerele complexe care au modulul egal cu 10
lab 5 -
lab 6 -
"""
import math


#nicely print a list
def print_list(lista:list[list[int]]):
    """
    afiseaza lista pe aceeasi linie cu spatiu intre elemente
    :param list: lista ce dorim sa fie afisata; preconditie: lista de tipul [1, 2, 3]
    :return: no return
    """
    for i in lista:
        print(i, end=" ")
    print()

def print_list_imaginary_number(lista:list[list[int]]):
    for i in lista:
        print(f"{i[0]} {i[1]}i", end=", ")

def read_complex_number()->list[int]:
    while True:
        try:
            parte_reala = int(input("Introdu partea reala a numarului pe care vrei sa il adaugi: "))
            parte_imaginara = int(input("Introdu partea imaginara (fara i) a numarului pe care vrei sa il adaugi: "))
            return [parte_reala, parte_imaginara]
        except ValueError:
            print("Valoare invalida, reintrodu numarul")

#add numbers to list - option 1
def read_index_to_add(lista:list[list[int]])->int:
    while True:
        try:
            index = int(input(f"Introdu index-ul unde doresti sa adaugi o valoare (intre 0 si {len(lista)-1}), introdu -1 pentru a adauga la final"))
            if index > len(lista) - 1 or index < -1:
                raise ValueError
            return index
        except ValueError:
            print("Introdu o valoare valida.")

def add_number_complex_to_list(lista:list[list[int]], index:int, number:list[int]):
    if index == -1:
        lista.append(number)
    else:
        lista.insert(index, number)

#modify elements in list - option 2
def read_index_to_remove_item(lista:list[list[int]])->int:
    while True:
        try:
            index = int(input(f"Introdu index-ul unde doresti sa stergi valoarea (intre 0 si {len(lista)-1})"))
            if index > len(lista) - 1 or index < 0:
                raise ValueError
            return index
        except ValueError:
            print("Introdu o valoare valida.")

def remove_element_on_index(lista:list[list[int]], index:int):
    lista.pop(index)

def read_indexes_to_remove_subsequence(lista:list[list[int]])->list[int]:
    index_start = 0
    index_end = 0
    while True:
        try:
            index_start = int(input(f"Introdu index-ul de unde doresti sa incepi a sterge valori (intre 0 si {len(lista)-1}) - indexul este inclus in stergere"))
            if index_start > len(lista) - 1 or index_start < 0:
                raise ValueError
            break
        except ValueError:
            print("Introdu o valoare valida.")
    while True:
        try:
            index_end = int(input(f"Introdu index-ul unde doresti sa opresti stergerea de valori (intre 0 si {len(lista)-1} si mai mare sau egal ca {index_start}) - indexul este inclus in stergere"))
            if index_end > len(lista) - 1 or index_end < 0 or index_end < index_start:
                raise ValueError
            break
        except ValueError:
            print("Introdu o valoare valida.")
    return [index_start, index_end]

def remove_elements_subsequence(lista:list[list[int]], indexes:list[int])->list[list[int]]:
    lista = lista[:indexes[0]] + lista[indexes[1]+1:]
    return lista

def replace_complex_value_with_another_one(lista:list[list[int]], to_be_replaced:list[int], to_replace:list[int]):
    for i in lista:
        if i == to_be_replaced:
            lista[i] = to_replace
    return lista

def print_menu_modify_elements():
    pass


#---------------------LAB 4
#search numbers - option 3
def read_indexes_to_print_imaginary_subsequence(lista:list[list[int]])->list[int]:
    index_start = 0
    index_end = 0
    while True:
        try:
            index_start = int(input(f"Introdu index-ul de unde doresti sa incepi afisarea (intre 0 si {len(lista)-1}) - indexul este inclus"))
            if index_start > len(lista) - 1 or index_start < 0:
                raise ValueError
            break
        except ValueError:
            print("Introdu o valoare valida.")
    while True:
        try:
            index_end = int(input(f"Introdu index-ul unde doresti sa opresti afisarea (intre 0 si {len(lista)-1} si mai mare sau egal ca {index_start}) - indexul este inclus"))
            if index_end > len(lista) - 1 or index_end < 0 or index_end < index_start:
                raise ValueError
            break
        except ValueError:
            print("Introdu o valoare valida.")
    return [index_start, index_end]


def print_imaginary_side(lista:list[list[int]], indexes_print:list[int]):
    for i in range(indexes_print[0], indexes_print[1] + 1):
        print(lista[i][1], end = " ")
    print()

def get_all_imaginary_numbers_where_abs_value_less_than_10(lista:list[list[int]])->list[list[int]]:
    return_value = []
    for i in lista:
        if(math.sqrt(i[0] ** 2 + i[1] ** 2) < 10):
            return_value.append(i)
    return return_value

def get_all_imaginary_numbers_where_abs_value_equals_10(lista:list[list[int]])->list[list[int]]:
    return_value = []
    for i in lista:
        if math.sqrt(i[0] ** 2 + i[1] ** 2) == 10:
            return_value.append(i)
    return return_value

def print_all_imaginary_numbers_where_abs_value_equals_10(lista:list[list[int]]):
    print_list_imaginary_number(get_all_imaginary_numbers_where_abs_value_equals_10(lista))

def print_all_imaginary_numbers_where_abs_value_less_than_10(lista:list[list[int]]):
    print_list_imaginary_number(get_all_imaginary_numbers_where_abs_value_less_than_10(lista))

#operations with numbers in the list - option 4
def subsequence_sum(lista:list[list[int]], start:int, end:int)->list[int]:
    sum = [0, 0]
    for i in range(start, end + 1):
        sum[0] += lista[i][0]
        sum[1] += lista[i][1]
    return sum

def subsequence_product(lista:list[list[int]], start:int, end:int)->list[int]:
    product = [1, 1]
    for i in range(start, end+1):
        product[0] = (product[0] * lista[i][0] - product[1] * lista[i][1])
        product[1] = (product[0] * lista[i][1] + product[1] * lista[i][0])
    return product

def get_sorted_list_by_imaginary_part(lista:list[list[int]])->list[list[int]]:
    def sorting_criteria(item:list[int]):
        return item[1]
    sorted_list = lista[:]
    sorted_list.sort(key = sorting_criteria)
    return sorted_list

#filtering - option 5
def prime_number(number:int)->bool:
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def remove_prime_real_part(lista:list[list[int]])->list[list[int]]:
    temp = []
    for i in range(len(lista)):
        if not prime_number(lista[i][0]):
            temp.append(lista[i])
    return temp

def remove_elements_where_abs_value_doesnt_satisfy_request(lista:list[list[int]], option:int, number:int)->list[list[int]]:
    return_list = []
    for i in lista:
        absolute_value = math.sqrt(i[0] ** 2 + i[1] ** 2)

        if option == 1 and absolute_value >= number:
            return_list.append(i)
        elif option == 2 and (absolute_value < number or absolute_value > number):
            return_list.append(i)
        elif option == 3 and absolute_value <= number:
            return_list.append(i)
    return return_list


#menu
def menu_interact()->int:
    while True:
        try:
            menu_option = int(input("Introdu o optiune din meniu pe care vrei sa o urmezi: \n"))
            if menu_option < 0 or menu_option > 6:
                raise ValueError
            return menu_option
        except ValueError:
            print("Introdu o valoare valida")

def print_menu():
    pass


def middleware_functions_list():
    pass


def main():
    elemente_citite = False
    list_main = []
    while True:
        menu_option = menu_interact()
        print_menu()
        if menu_option == 1:
            add_number_complex_to_list(list_main)
            print("Noua lista este: \n")
            print_list(list_main)
        elif menu_option == 2:
            option = menu_interact()
    print("bye bye")

"""
add testing for (3 - 5)
add documentation (3 - 5)
add the tasks things (3 - 5)
implement the menu options for 3 - 5 options
check on how I can structure the menu and implement the first 2 functionalities as well (optional)
make the functionality 6
"""