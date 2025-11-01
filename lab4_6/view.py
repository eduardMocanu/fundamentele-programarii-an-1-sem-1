from controller import *

def new_list_message():
    """
    afiseaza un mesaj
    :return: no return
    """
    print("Lista ta este:")

def print_list_complex_number(lista:list[dict[str, int]]):
    """
    afiseaza partea imaginara a unor numere complexe din lista
    :param lista: lista pentru care dorim sa afisam; de tipul: [[1, 2], [3, 4]]
    :return: no return
    """
    for i in lista:
        print(f"{get_real_part_complex_element(i)} {get_imaginary_part_complex_element(i)}i", end="; ")
    print()

def read_complex_number()-> dict[str, int]:
    """
    permite introducerea de la tastatura a unui numar complex
    :return: numarul citit; de tipu: [1, 2] - 1 parte reala; 2 - parte imaginara
    """
    while True:
        try:
            parte_reala = int(input("Introdu partea reala a numarului pe care vrei sa il citesti: "))
            parte_imaginara = int(input("Introdu partea imaginara (fara i) a numarului pe care vrei sa il citesti: "))
            return create_complex_number(parte_reala, parte_imaginara)
        except ValueError:
            print("Valoare invalida, reintrodu numarul")

def read_2_indexes_start_end(lista:list[dict[str, int]])->list[int]:
    """
    Citeste 2 pozitii din lista inceputul, respectiv sfarsitul
    :param lista: lista pentru care dorim sa citim cei 2 indici; de tipul: [[1, 2], [3, 4]]
    :return: o lista ce contine indexul de start pe pozitia 0 si indexul de sfarsit pe pozitia 1
    """
    index_start = 0
    index_end = 0
    while True:
        try:
            index_start = int(input(f"Introdu index-ul de unde doresti sa incepi (intre 0 si {len(lista)-1}) - indexul este inclus: "))
            if index_start > len(lista)-1 or index_start < 0:
                raise ValueError
            break
        except ValueError:
            print("Introdu o valoare valida.")
    while True:
        try:
            index_end = int(input(f"Introdu index-ul unde doresti sa te opresti (intre 0 si {len(lista)-1} si mai mare sau egal ca {index_start}) - indexul este inclus: "))
            if index_end > len(lista)-1 or index_end < 0 or index_end < index_start:
                raise ValueError
            break
        except ValueError:
            print("Introdu o valoare valida.")
    return [index_start, index_end]


def read_whole_number()->int:
    """
    permite citirea unui numar intreg de la tastatura
    :return: numarul citit care este garantat un int
    """
    while True:
        try:
            number = int(input("Introdu numarul: \n"))
            return number
        except ValueError:
            print("Introdu o valoare valida")

def read_index_to_add(lista:list[dict[str, int]])->int:
    """
    permite citirea unui index (valabil pentru lista) index >= 0 si index < len(lista)
    :param lista: lista pentru care dorim sa citim un index
    :return: indexul citit
    """
    while True:
        try:
            index = int(input(f"Introdu index-ul unde doresti sa adaugi o valoare (intre 0 si {len(lista)}), introdu -1 pentru a adauga la final: "))
            if index > len(lista) or index < -1:
                raise ValueError
            return index
        except ValueError:
            print("Introdu o valoare valida.")

def read_index_to_remove_item(lista:list[dict[str, int]])->int:
    """
    permite citirea unui index dintr-o lista pentru a oferi pozitia pe care dorim sa eliminam un element
    :param lista: lista de unde dorim sa citim un astfel de index
    :return: indexul citit
    """
    while True:
        try:
            index = int(input(f"Introdu index-ul unde doresti sa stergi valoarea (intre 0 si {len(lista)-1})"))
            if index > len(lista) - 1 or index < 0:
                raise ValueError
            return index
        except ValueError:
            print("Introdu o valoare valida.")

def print_imaginary_side(lista:list[dict[str, int]], indexes_print:list[int]):
    """
    Afiseaza partea imaginara a numerelor cuprinse intre 2 pozitii
    :param lista: lista din care dorim sa afisam elementele; de tipul: [[1, 2], [3, 4]]
    :param indexes_print: o lista de 2 elemente care contine pe pozitia 0 indexul de start iar pe pozitia 1 ultimul index; de tipul: [1, 2]
    :return: no return
    """
    for i in range(indexes_print[0], indexes_print[1] + 1):
        print(get_imaginary_part_complex_element(lista[i]), end = " ")
    print()


def print_all_imaginary_numbers_where_abs_value_equals_10(lista:list[dict[str, int]]):
    """
    Afiseaza sublista dintr-o lista de numere complexe unde toate elementele au valoarea absoluta egala cu 10
    :param lista: lista unde dorim sa gasim o sublista care sa satisfaca conditia ca toate elementele sa aiba valoarea absoluta egala cu 10 si sa afiseze sublista construita; de tipul: [[1, 2], [3, 4]]
    :return: no return
    """
    print_list_complex_number(get_all_imaginary_numbers_where_abs_value_equals_10(lista))

def print_all_imaginary_numbers_where_abs_value_less_than_10(lista:list[dict[str, int]]):
    """
    Afiseaza sublista dintr-o lista de numere complexe unde toate elementele au valoarea absoluta mai mica decat 10
    :param lista: lista unde dorim sa gasim o sublista care sa satisfaca conditia ca toate elementele sa aiba valoarea absoluta mai mica decat 10 si sa afiseze sublista construita; de tipul: [[1, 2], [3, 4]]
    :return: no return
    """
    print_list_complex_number(get_all_imaginary_numbers_where_abs_value_less_than_10(lista))

#menu
def menu_interact(maximum_option:int)->int:
    """
    Citeste optiunea pe care doresti sa o urmezi in program
    :return: optiunea introdusa, sub forma de numar (int)
    """
    while True:
        try:
            menu_option = int(input("Introdu o optiune din meniu pe care vrei sa o urmezi: \n"))
            if menu_option < 0 or menu_option > maximum_option:
                raise ValueError
            return menu_option
        except ValueError:
            print("Introdu o valoare valida")

def print_menu_option_1():
    """Afișează opțiunile pentru adăugarea numerelor complexe în listă.
    :return: no return"""
    print("1. ADAUGA NUMAR COMPLEX LA SFARSITUL LISTEI")
    print("2. INSERARE NUMAR COMPLEX PE O POZITIE DATA")


def print_menu_option_2():
    """Afișează opțiunile pentru modificarea elementelor din listă.
    :return: no return"""
    print("1. STERGE ELEMENT DE PE O POZITIE DATA")
    print("2. STERGE ELEMENTELE DE PE UN INTERVAL DE POZITII")
    print("3. INLOCUIESTE TOATE APARITIILE UNUI NUMAR COMPLEX CU UN ALT NUMAR COMPLEX")


def print_menu_option_3():
    """Afișează opțiunile pentru afișarea și filtrarea numerelor complexe.
    :return: no return"""
    print("1. TIPARESTE PARTEA IMAGINARA PENTRU NUMERELE DIN LISTA (se da un interval de pozitii)")
    print("2. TIPARESTE TOATE NUMERELE COMPLEXE CARE AU MODULUL MAI MIC DECAT 10")
    print("3. TIPARESTE TOATE NUMERELE COMPLEXE CARE AU MODULUL EGAL CU 10")


def print_menu_option_4():
    """Afișează opțiunile pentru efectuarea operațiilor matematice asupra listei.
    :return: no return"""
    print("1. SUMA NUMERELOR INTRE 2 INDICI")
    print("2. PRODUSUL NUMERELOR INTRE 2 INDICI")
    print("3. TIPARESTE LISTA SORTATA DESCRESCATOR DUPA PARTEA IMAGINARA")


def print_menu_option_5():
    """Afișează opțiunile pentru filtrarea numerelor complexe.
    :return: no return"""
    print("1. ELIMINA DIN LISTA NUMERELE COMPLEXE LA CARE PARTEA REALA ESTE NUMAR PRIM")
    print("2. ELIMINA DIN LISTA NUMERELE COMPLEXE LA CARE MODULUL ESTE <, =, > DECAT UN NUMAR DAT")


def print_submenu_option_5():
    """Afișează submeniul pentru condițiile de filtrare (<, =, >).
    :return: no return"""
    print("1. <")
    print("2. =")
    print("3. >")


def print_main_menu():
    """Afișează meniul principal al aplicației.
    :return: no return"""
    print("0. IESIRE (poate fi introdus oricand pentru a opri programul)")
    print("1. ADAUGA NUMAR IN LISTA")
    print("2. MODIFICA ELEMENTE DIN LISTA")
    print("3. CAUTARE NUMERE")
    print("4. OPERATII CU NUMERELE DIN LISTA")
    print("5. FILTRARE")
    print("6. UNDO")
