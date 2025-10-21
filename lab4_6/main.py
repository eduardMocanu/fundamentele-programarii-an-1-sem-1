"""
Cerințe generale:
• Documentația trebuie să conțină: scenarii de rulare

Enunt:
Creați un program care lucrează cu numere complexe (a + bi). Programul
gestionează o listă de numere complexe și permite efectuarea repetată a
următoarelor acțiuni:
Functionalitati:
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
4. Operații cu numerele din listă
• suma numerelor dintr-o subsecventă dată (se da poziția de început și
sfârșit).
• Produsul numerelor dintr-o subsecventă dată (se da poziția de început
și sfârșit).
• Tipărește lista sortată descrescător după partea imaginara
5. Filtrare.
• Filtrare parte reala prim – elimină din listă numerele complexe la care
partea reala este prim.
• Filtrare modul – elimina din lista numerele complexe la care modulul
este <,= sau > decât un număr dat.
6. Undo
• Reface ultima operație (lista de numere revine la numerele ce existau
înainte de ultima operație care a modificat lista) – Nu folosiți funcția
deepCopy

Tasks:
 • Adaugă număr complex la sfârșitul listei
 • Inserare număr complex pe o poziție dată.
 • Șterge element de pe o poziție dată.
 • Șterge elementele de pe un interval de poziții.
 • Înlocuiește toate aparițiile unui număr complex cu un alt număr
complex.
 • Tipărește partea imaginara pentru numerele din listă. Se dă intervalul
de poziții (sub secvența).
 • Tipărește toate numerele complexe care au modulul mai mic decât 10
 • Tipărește toate numerele complexe care au modulul egal cu 10
• Calculează media scorurilor pentru un interval dat (ex. Se da 1 și 5 se
tipărește media scorurilor participanților 1,2,3,4 și 5
• Calculează scorul minim pentru un interval de participanți dat.
• Tipărește participanții dintr-un interval dat care au scorul multiplu de 10.
• Filtrare participanți care au scorul multiplu unui număr dat. Ex. Se da
numărul 10, se elimină scorul de la toți participanții care nu au scorul
multiplu de 10.
• Filtrare participanți care au scorul mai mic decât un scor dat.


lab 4 - iteratia 1
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
4. Operații pe un subset de participanți.
• Calculează media scorurilor pentru un interval dat (ex. Se da 1 și 5 se
tipărește media scorurilor participanților 1,2,3,4 și 5
• Calculează scorul minim pentru un interval de participanți dat.
• Tipărește participanții dintr-un interval dat care au scorul multiplu de 10.
5. Filtrare.
• Filtrare participanți care au scorul multiplu unui număr dat. Ex. Se da
numărul 10, se elimină scorul de la toți participanții care nu au scorul
multiplu de 10.
• Filtrare participanți care au scorul mai mic decât un scor dat.
lab 5 -
lab 6 -
"""
import math

#utilities
def new_list_message():
    """
    afiseaza un mesaj
    :return: no return
    """
    print("Lista ta este:")

def print_list_imaginary_number(lista:list[list[int]]):
    """
    afiseaza partea imaginara a unor numere complexe din lista
    :param lista: lista pentru care dorim sa afisam; de tipul: [[1, 2], [3, 4]]
    :return: no return
    """
    for i in lista:
        print(f"{i[0]} {i[1]}i", end="; ")
    print()

def read_complex_number()->list[int]:
    """
    permite introducerea de la tastatura a unui numar complex
    :return: numarul citit; de tipu: [1, 2] - 1 parte reala; 2 - parte imaginara
    """
    while True:
        try:
            parte_reala = int(input("Introdu partea reala a numarului pe care vrei sa il citesti: "))
            parte_imaginara = int(input("Introdu partea imaginara (fara i) a numarului pe care vrei sa il citesti: "))
            return [parte_reala, parte_imaginara]
        except ValueError:
            print("Valoare invalida, reintrodu numarul")

def read_2_indexes_start_end(lista:list[list[int]])->list[int]:
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

def prime_number(number:int)->bool:
    """
    Verifica daca un numar introdus este prim
    :param number: numarul pe care dorim sa il verificam daca este prim
    :return: true - este prim / false - nu este prim
    """
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def test_prime_number():
    """
    Testeaza functionalitatea corecta a functiei prime_number
    :return: no return
    """
    assert prime_number(1) == False
    assert prime_number(2) == True
    assert prime_number(3) == True
    assert prime_number(4) == False

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

#add numbers to list - option 1
def read_index_to_add(lista:list[list[int]])->int:
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

def add_number_complex_to_list(lista:list[list[int]], index:int, number:list[int])->list[list[int]]:
    """
    adauga un numar complex la o lista; de tipul: [[1, 2], [2, 3]]
    :param lista: lista in care dorim sa adaugam numarul
    :param index: pozitia in care dorim sa adaugam numarul
    :param number: numarul pe care dorim sa il adaugam
    :return: lista cu numarul adaugat pe pozitia dorita
    """
    lista_temp = lista[:]
    if index == -1:
        lista_temp.append(number)
    else:
        lista_temp.insert(index, number)
    return lista_temp

def test_add_number_complex_to_list():
    """
    testeaza functionalitatea corecta a functiei add_number_complex_to_list
    :return: no return
    """
    assert add_number_complex_to_list([[1, 2], [3, 4]], -1, [5, 6]) == [[1, 2], [3, 4], [5, 6]]
    assert add_number_complex_to_list([[1, 2], [3, 4]], 0, [5, 6]) == [[5, 6], [1, 2], [3, 4]]
    assert add_number_complex_to_list([[1, 2], [3, 4]], 1, [5, 6]) == [[1, 2], [5, 6], [3, 4]]

#modify elements in list - option 2
def read_index_to_remove_item(lista:list[list[int]])->int:
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

def remove_element_on_index(lista:list[list[int]], index:int)->list[list[int]]:
    """
    elimina un element din lista la o pozitie data
    :param lista: lista de unde dorim sa stergem elementul
    :param index: indexul unde dorim sa stergem elementul
    :return: lista modificata (cu elementul sters)
    """
    lista_temp = lista[:]
    lista_temp.pop(index)
    return lista_temp

def test_remove_element_on_index():
    """
    permite testearea functionalitatii corecte a functiei remove_element_on_index
    :return: no return
    """
    assert remove_element_on_index([[1, 2], [3, 4]], 0) == [[3, 4]]
    assert remove_element_on_index([[1, 2], [3, 4], [5, 6]], 1) == [[1, 2], [5, 6]]
    assert remove_element_on_index([[1, 2], [3, 4], [5, 6]], 2) == [[1, 2], [3, 4]]


def remove_elements_subsequence(lista:list[list[int]], index_start:int, index_end:int)->list[list[int]]:
    """
    Permite eliminarea unei subsecvente din lista intre 2 indici
    :param lista: lista din care dorim sa eliminam o subsecventa
    :param index_start: indexul de start de unde incepe stergerea
    :param index_end: indexul unde dorim sa oprim stergerea
    :return: lista cu subsecventa eliminata
    """
    lista = lista[:index_start] + lista[index_end + 1:]
    return lista

def test_remove_elements_subsequence():
    """
    testeaza functionalitatea corecta a functiei remove_elements_subsequence
    :return: no return
    """
    assert remove_elements_subsequence([[1, 2], [2, 3]], 0, 1) == []
    assert remove_elements_subsequence([[1, 2], [2, 3], [4, 5]], 0, 1) == [[4, 5]]
    assert remove_elements_subsequence([], 10, 11) == []


def replace_complex_value_with_another_one(lista:list[list[int]], to_be_replaced:list[int], to_replace:list[int])->list[list[int]]:
    """
    permite inlocuirea tuturor prezentelor unui numar complex cu un altul
    :param lista: lista in care dorim sa inlocuim valoarea unui numar complex
    :param to_be_replaced: valoarea care trebuie inlocuita
    :param to_replace: valoarea cu care se inlocuieste
    :return: lista modificata
    """
    lista_temp = lista[:]
    for i in range(len(lista)):
        if lista_temp[i] == to_be_replaced:
            lista_temp[i] = to_replace
    return lista_temp

def test_replace_complex_value_with_another_one():
    """
    testeaza functionalitatea corecta a functiei replace_complex_value_with_another_one
    :return: no return
    """
    assert replace_complex_value_with_another_one([[1, 2], [3, 4]], [1, 2], [10, 11]) == [[10, 11], [3, 4]]
    assert replace_complex_value_with_another_one([[1, 2], [3, 4], [5, 6], [5, 6], [5, 6]], [5, 6], [1, 4]) == [[1, 2], [3, 4], [1, 4], [1, 4], [1, 4]]
    assert replace_complex_value_with_another_one([], [5, 6], [1, 4]) == []


#---------------------LAB 4
#search numbers - option 3

def print_imaginary_side(lista:list[list[int]], indexes_print:list[int]):
    """
    Afiseaza partea imaginara a numerelor cuprinse intre 2 pozitii
    :param lista: lista din care dorim sa afisam elementele; de tipul: [[1, 2], [3, 4]]
    :param indexes_print: o lista de 2 elemente care contine pe pozitia 0 indexul de start iar pe pozitia 1 ultimul index; de tipul: [1, 2]
    :return: no return
    """
    for i in range(indexes_print[0], indexes_print[1] + 1):
        print(lista[i][1], end = " ")
    print()

def get_all_imaginary_numbers_where_abs_value_less_than_10(lista:list[list[int]])->list[list[int]]:
    """
    Gaseste o sublista care contine toate elementele dintr-o lista de numere complexe care au valoarea absoluta mai mica decat 10
    :param lista: lista de unde dorim a extrage valorile cu modulul mai mic decat 10; de tipul: [[1, 2], [3, 4]]
    :return: sublista care contine elementele care satisfac cerinta
    """
    return_value = []
    for i in lista:
        if math.sqrt(i[0] ** 2 + i[1] ** 2) < 10:
            return_value.append(i)
    return return_value

def test_get_all_imaginary_numbers_where_abs_value_less_than_10():
    """
    Testeaza functionalitatea corecta a functiei get_all_imaginary_numbers_where_abs_value_less_than_10
    :return: no return
    """
    assert get_all_imaginary_numbers_where_abs_value_less_than_10([[1, 2], [6, 7]]) == [[1, 2], [6, 7]]
    assert get_all_imaginary_numbers_where_abs_value_less_than_10([[1, 2], [100, 101]]) == [[1, 2]]
    assert get_all_imaginary_numbers_where_abs_value_less_than_10([]) == []


def get_all_imaginary_numbers_where_abs_value_equals_10(lista:list[list[int]])->list[list[int]]:
    """
    Gaseste o sublista dintr-o lista de numere complexe oferita, unde toate elementele au valoarea absoluta egala cu 10; de tipul: [[1, 2], [3, 4]]
    :param lista: lista unde dorim sa gasim sublista care are toate elementele cu proprietatea ca valoarea lor absoluta este 10; de tipul: [[1, 2], [3, 4]]
    :return: sublista construita cu proprietatea precizata
    """
    return_value = []
    for i in lista:
        if math.sqrt(i[0] ** 2 + i[1] ** 2) == 10:
            return_value.append(i)
    return return_value

def test_get_all_imaginary_numbers_where_abs_value_equals_10():
    """
    Testeaza functionalitatea corecta a functiei get_all_imaginary_numbers_where_abs_value_equals_10
    :return: no return
    """
    assert get_all_imaginary_numbers_where_abs_value_equals_10([[1, 2], [6, 8]]) == [[6, 8]]
    assert get_all_imaginary_numbers_where_abs_value_equals_10([[1, 2], [100, 101]]) == []
    assert get_all_imaginary_numbers_where_abs_value_equals_10([]) == []

def print_all_imaginary_numbers_where_abs_value_equals_10(lista:list[list[int]]):
    """
    Afiseaza sublista dintr-o lista de numere complexe unde toate elementele au valoarea absoluta egala cu 10
    :param lista: lista unde dorim sa gasim o sublista care sa satisfaca conditia ca toate elementele sa aiba valoarea absoluta egala cu 10 si sa afiseze sublista construita; de tipul: [[1, 2], [3, 4]]
    :return: no return
    """
    print_list_imaginary_number(get_all_imaginary_numbers_where_abs_value_equals_10(lista))

def print_all_imaginary_numbers_where_abs_value_less_than_10(lista:list[list[int]]):
    """
    Afiseaza sublista dintr-o lista de numere complexe unde toate elementele au valoarea absoluta mai mica decat 10
    :param lista: lista unde dorim sa gasim o sublista care sa satisfaca conditia ca toate elementele sa aiba valoarea absoluta mai mica decat 10 si sa afiseze sublista construita; de tipul: [[1, 2], [3, 4]]
    :return: no return
    """
    print_list_imaginary_number(get_all_imaginary_numbers_where_abs_value_less_than_10(lista))

#operations with numbers in the list - option 4

def subsequence_sum(lista:list[list[int]], start:int, end:int)->list[int]:
    """
    Calculeaza suma unei subsecvente de numere complexe dintr-o lista
    :param lista: lista unde dorim sa calculam suma; de tipul: [[1, 2], [3, 4]]
    :param start: indexul de unde dorim sa incepem sa calculam suma
    :param end: indexul unde dorim sa incetam sa calculam suma
    :return: lista de 2 elemente care contine suma elementelor reale pe indexul 0, iar pe indexul 1 suma numerelor imaginare
    """
    suma = [0, 0]
    end = min(end+1, len(lista))
    for i in range(start, end):
        suma[0] += lista[i][0]
        suma[1] += lista[i][1]
    return suma

def test_subsequence_sum():
    """
    Testeaza functionalitatea corecta a functiei subsequence_sum
    :return: no return
    """
    assert subsequence_sum([[1, 2], [3, 4], [5, 6]], 0, 2) == [9, 12]
    assert subsequence_sum([[4, 5], [6, 7]], 0, 0) == [4, 5]
    assert subsequence_sum([], 0, 100) == [0, 0]


def subsequence_product(lista: list[list[int]], start: int, end: int) -> list[int]:
    """
    Calculeaza produsul unei subsecvente de numere complexe dintr-o lista
    :param lista: lista unde dorim sa calculam produsul; de tipul: [[1, 2], [3, 4]]
    :param start: indexul de unde dorim sa incepem sa calculam produsul
    :param end: indexul unde dorim sa incetam sa calculam produsul
    :return: lista de 2 elemente care contine partea reala a produsului pe indexul 0, iar pe indexul 1 partea imaginara
    """
    product = [1, 0]
    end = min(end + 1, len(lista))
    for i in range(start, end):
        a, b = product
        c, d = lista[i]
        product[0] = a * c - b * d
        product[1] = a * d + b * c
    return product

def test_subsequence_product():
    """
    Testeaza functionalitatea corecta a functiei subsequence_product
    :return: no return
    """
    assert subsequence_product([[2, 3]], 0, 0) == [2, 3]
    assert subsequence_product([[2, 3], [1, 1]], 0, 1) == [-1, 5]
    assert subsequence_product([[1, 1], [2, 0], [0, 1]], 0, 2) == [-2, 2]

def get_sorted_list_by_imaginary_part(lista:list[list[int]])->list[list[int]]:
    """
    Ordoneaza descrescator o lista de numere complexe dupa partea imaginara
    :param lista: lista pe care dorim sa o ordonam; de tipul: [[1, 2], [3, 4]]
    :return: lista ce contine elementele ordonate
    """
    def sorting_criteria(item:list[int]):
        return item[1]
    sorted_list = lista[:]
    sorted_list.sort(reverse=True, key = sorting_criteria)
    return sorted_list

def test_get_sorted_list_by_imaginary_part():
    """
    Testeaza functionalitatea corecta a functiei get_sorted_list_by_imaginary_part
    :return: no return
    """
    assert  get_sorted_list_by_imaginary_part([[1, 2], [3, 4], [1, 1]]) == [[3, 4], [1, 2], [1, 1]]
    assert get_sorted_list_by_imaginary_part([[1, 1], [2, 2], [3, 3]]) == [[3, 3], [2,2], [1, 1]]
    assert get_sorted_list_by_imaginary_part([]) == []


#filtering - option 5
def remove_prime_real_part(lista:list[list[int]])->list[list[int]]:
    """
    Elimina numerele complexe care au partea reala numar prim dintr-o lista
    :param lista: lista de unde dorim sa eliminam numerele; de tipul: [[1, 2], [3, 4]]
    :return: lista rezultata dupa eliminarea elementelor care au partea reala numar prim
    """
    temp = []
    for i in range(len(lista)):
        if not prime_number(lista[i][0]):
            temp.append(lista[i])
    return temp

def test_remove_prime_real_part():
    """
    Testeaza functionalitatea corecta a functiei remove_prime_real_part
    :return: no return
    """
    assert remove_prime_real_part([[1, 2], [3, 4], [4, 5]]) == [[1, 2], [4, 5]]
    assert remove_prime_real_part([[4, 5], [6, 7], [8,9]]) == [[4, 5], [6, 7], [8, 9]]
    assert remove_prime_real_part([]) == []

def remove_elements_where_abs_value_doesnt_satisfy_request(lista:list[list[int]], option:int, number:int)->list[list[int]]:
    """
    Elimina numerele dintr-o lista ale caror valori absolute nu indeplinesc o conditie introdusa:
        1. sunt mai mici decat un numar
        2. sunt egale cu un numar
        3. sunt mai mari decat un numar
    :param lista: lista unde dorim sa eliminam elemente; de tipul: [[1, 2], [3, 4]]
    :param option: optiunea pe care o alegem pentru a filtra numerele
    :param number: numarul la care ne raportam pentru conditia introdusa
    :return: o sublista din ce initiala unde au fost filtrate elementele care nu satisfac conditia
    """
    return_list = []
    for i in lista:
        absolute_value = math.sqrt(i[0] ** 2 + i[1] ** 2)
        if option == 1 and absolute_value >= number:
            return_list.append(i)
        elif option == 2 and absolute_value != number:
            return_list.append(i)
        elif option == 3 and absolute_value <= number:
            return_list.append(i)
    return return_list

def test_remove_elements_where_abs_value_doesnt_satisfy_request():
    """
    Testeaza functionalitatea corecta a functiei remove_elements_where_abs_value_doesnt_satisfy_request
    :return: no return
    """
    data = [[3, 4], [1, 2], [0, 0], [5, 12]]
    assert remove_elements_where_abs_value_doesnt_satisfy_request(data, 1, 5) == [[3, 4], [5, 12]]
    assert remove_elements_where_abs_value_doesnt_satisfy_request(data, 2, 5) == [[1, 2], [0, 0], [5, 12]]
    assert remove_elements_where_abs_value_doesnt_satisfy_request(data, 3, 5) == [[3, 4], [1, 2], [0, 0]]
    assert remove_elements_where_abs_value_doesnt_satisfy_request([], 1, 5) == []
    assert remove_elements_where_abs_value_doesnt_satisfy_request([[3, 4]], 3, 6) == [[3, 4]]

def test_function():
    """
    ruleaza toate testele prezente in program pentru a se asigura ca functionalitatile sunt corecte
    :return: no return
    """
    test_get_all_imaginary_numbers_where_abs_value_equals_10()
    test_get_all_imaginary_numbers_where_abs_value_less_than_10()
    test_prime_number()
    test_get_sorted_list_by_imaginary_part()
    test_subsequence_product()
    test_subsequence_sum()
    test_remove_prime_real_part()
    test_remove_elements_where_abs_value_doesnt_satisfy_request()
    test_replace_complex_value_with_another_one()
    test_remove_elements_subsequence()
    test_add_number_complex_to_list()
    test_remove_element_on_index()
    test_replace_complex_value_with_another_one()


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


def middleware_functions_list(has_elements: bool) -> bool:
    """
    Verifică dacă lista conține elemente înainte de a continua execuția.
    :param has_elements: False dacă lista este goală, True dacă are elemente.
    :return: False dacă lista este goală, True dacă se poate continua.
    """
    if not has_elements:
        print("Mai intai populeaza lista")
        return False
    return True

def check_list_length(lista:list[list[int]]) -> bool:
    """
    Verifica daca o lista este goala sau nu
    :param lista: lista unde dorim sa verificam daca este goala sau nu
    :return: True - nu este goala; False - este goala
    """
    if len(lista) == 0:
        return False
    return True

def main():
    elemente_citite = False
    list_main = []
    while True:
        print_main_menu()
        menu_option = menu_interact(6)
        elemente_citite = check_list_length(list_main)
        if menu_option == 0:
            break
        elif menu_option == 1:
            print_menu_option_1()
            option = menu_interact(2)
            if option == 0:
                break
            elif option == 1:
                number = read_complex_number()
                list_main = add_number_complex_to_list(list_main, -1, number)
                new_list_message()
                print_list_imaginary_number(list_main)
            elif option == 2:
                number = read_complex_number()
                index = read_index_to_add(list_main)
                list_main = add_number_complex_to_list(list_main, index, number)
                new_list_message()
                print_list_imaginary_number(list_main)
        elif middleware_functions_list(elemente_citite):
            if menu_option == 2:
                pass
            elif menu_option == 3:
                print_menu_option_3()
                option = menu_interact(3)
                if option == 0:
                    break
                elif option == 1:
                    indexes = read_2_indexes_start_end(list_main)
                    new_list_message()
                    print_imaginary_side(list_main, indexes)
                elif option == 2:
                    new_list_message()
                    print_all_imaginary_numbers_where_abs_value_less_than_10(list_main)
                elif option == 3:
                    new_list_message()
                    print_all_imaginary_numbers_where_abs_value_equals_10(list_main)
            elif menu_option == 4:
                print_menu_option_4()
                option = menu_interact(3)
                if option ==0:
                    break
                elif option == 1:
                    indexes = read_2_indexes_start_end(list_main)
                    suma = subsequence_sum(list_main, indexes[0], indexes[1])
                    print(f"suma este: {suma[0]} {suma[1]}i")
                elif option == 2:
                    indexes = read_2_indexes_start_end(list_main)
                    product = subsequence_product(list_main, indexes[0], indexes[1])
                    print(f"produsul este: {product[0]} {product[1]}i")
                elif option == 3:
                    new_list_message()
                    print_list_imaginary_number(get_sorted_list_by_imaginary_part(list_main))
            elif menu_option == 5:
                print_menu_option_5()
                option = menu_interact(2)
                if option == 0:
                    break
                elif option == 1:
                    list_main = remove_prime_real_part(list_main)[:]
                    new_list_message()
                    print_list_imaginary_number(list_main)
                elif option == 2:
                    print_submenu_option_5()
                    submenu = menu_interact(3)
                    print("Numarul cu care doresti sa compari este: ")
                    number = read_whole_number()
                    list_main = remove_elements_where_abs_value_doesnt_satisfy_request(list_main, submenu, number)[:]
                    new_list_message()
                    print_list_imaginary_number(list_main)

    print("bye bye")

"""
check on how I can structure the menu and implement the first 2 functionalities as well (optional)
make the functionality 6 (optional)
"""
test_function()
main()