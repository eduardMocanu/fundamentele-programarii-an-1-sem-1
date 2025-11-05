from class_like import *
import math

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

def add_number_complex_to_list(lista:list[dict[str, int]], index:int, number:dict[str, int])->list[dict[str, int]]:
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

def remove_element_on_index(lista:list[dict[str, int]], index:int)->list[dict[str, int]]:
    """
    elimina un element din lista la o pozitie data
    :param lista: lista de unde dorim sa stergem elementul
    :param index: indexul unde dorim sa stergem elementul
    :return: lista modificata (cu elementul sters)
    """
    lista_temp = lista[:]
    lista_temp.pop(index)
    return lista_temp


def remove_elements_subsequence(lista:list[dict[str, int]], index_start:int, index_end:int)->list[dict[str, int]]:
    """
    Permite eliminarea unei subsecvente din lista intre 2 indici
    :param lista: lista din care dorim sa eliminam o subsecventa
    :param index_start: indexul de start de unde incepe stergerea
    :param index_end: indexul unde dorim sa oprim stergerea
    :return: lista cu subsecventa eliminata
    """
    lista = lista[:index_start] + lista[index_end + 1:]
    return lista

def replace_complex_value_with_another_one(lista:list[dict[str, int]], to_be_replaced:dict[str, int], to_replace:dict[str, int])->list[dict[str, int]]:
    """
    permite inlocuirea tuturor prezentelor unui numar complex cu un altul
    :param lista: lista in care dorim sa inlocuim valoarea unui numar complex
    :param to_be_replaced: valoarea care trebuie inlocuita
    :param to_replace: valoarea cu care se inlocuieste
    :return: lista modificata
    """
    lista_temp = lista
    for i in range(len(lista)):
        if lista_temp[i] == to_be_replaced:
            set_imag_part_complex_element(lista_temp[i], to_replace["imag"])
            set_real_part_complex_element(lista_temp[i], to_replace["real"])
    return lista_temp

def get_all_imaginary_numbers_where_abs_value_less_than_10(lista:list[dict[str, int]])->list[dict[str, int]]:
    """
    Gaseste o sublista care contine toate elementele dintr-o lista de numere complexe care au valoarea absoluta mai mica decat 10
    :param lista: lista de unde dorim a extrage valorile cu modulul mai mic decat 10; de tipul: [[1, 2], [3, 4]]
    :return: sublista care contine elementele care satisfac cerinta
    """
    return_value = []
    for i in lista:
        if math.sqrt(get_real_part_complex_element(i) ** 2 + get_imaginary_part_complex_element(i) ** 2) < 10:
            return_value.append(i)
    return return_value

def get_all_imaginary_numbers_where_abs_value_equals_10(lista:list[dict[str, int]])->list[dict[str, int]]:
    """
    Gaseste o sublista dintr-o lista de numere complexe oferita, unde toate elementele au valoarea absoluta egala cu 10; de tipul: [[1, 2], [3, 4]]
    :param lista: lista unde dorim sa gasim sublista care are toate elementele cu proprietatea ca valoarea lor absoluta este 10; de tipul: [[1, 2], [3, 4]]
    :return: sublista construita cu proprietatea precizata
    """
    return_value = []
    for i in lista:
        if math.sqrt(get_real_part_complex_element(i) ** 2 + get_imaginary_part_complex_element(i) ** 2) == 10:
            return_value.append(i)
    return return_value

def subsequence_sum(lista:list[dict[str, int]], start:int, end:int)->list[int]:
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
        suma[0] += get_real_part_complex_element(lista[i])
        suma[1] += get_imaginary_part_complex_element(lista[i])
    return suma

def subsequence_product(lista: list[dict[str, int]], start: int, end: int) -> dict[str, int]:
    """
    Calculează produsul unei subsecvente de numere complexe dintr-o listă
    """
    product = create_complex_number(1, 0)  # start with 1 + 0i
    end = min(end + 1, len(lista))
    for i in range(start, end):
        a, b = get_real_part_complex_element(product), get_imaginary_part_complex_element(product)
        c, d = get_real_part_complex_element(lista[i]), get_imaginary_part_complex_element(lista[i])
        set_real_part_complex_element(product, a * c - b * d)
        set_imag_part_complex_element(product, a * d + b * c)
    return product

def get_sorted_list_by_imaginary_part(lista:list[dict[str, int]])->list[dict[str, int]]:
    """
    Ordoneaza descrescator o lista de numere complexe dupa partea imaginara
    :param lista: lista pe care dorim sa o ordonam; de tipul: [[1, 2], [3, 4]]
    :return: lista ce contine elementele ordonate
    """
    def sorting_criteria(item:dict[str, int]):
        return get_imaginary_part_complex_element(item)
    sorted_list = lista[:]
    sorted_list.sort(reverse=True, key = sorting_criteria)
    return sorted_list

def remove_prime_real_part(lista:list[dict[str, int]])->list[dict[str, int]]:
    """
    Elimina numerele complexe care au partea reala numar prim dintr-o lista
    :param lista: lista de unde dorim sa eliminam numerele; de tipul: [[1, 2], [3, 4]]
    :return: lista rezultata dupa eliminarea elementelor care au partea reala numar prim
    """
    temp = []
    for i in range(len(lista)):
        if not prime_number(get_real_part_complex_element(lista[i])):
            temp.append(lista[i])
    return temp

def remove_elements_where_abs_value_doesnt_satisfy_request(lista:list[dict[str, int]], option:int, number:int)->list[dict[str, int]]:
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
        absolute_value = math.sqrt(get_real_part_complex_element(i) ** 2 + get_imaginary_part_complex_element(i) ** 2)
        if option == 1 and absolute_value >= number:
            return_list.append(i)
        elif option == 2 and absolute_value != number:
            return_list.append(i)
        elif option == 3 and absolute_value <= number:
            return_list.append(i)
    return return_list

def get_list_before_last_change(history_list:list[list[dict[str, int]]])->list[dict[str, int]]:
    """
    Returneaza lista care exista inainte de ultima modificare
    :param history_list: istoricul de modificari al listei
    :return: ultima lista inainte de modificare
    """
    if len(history_list) > 1:
        history_list.pop()
        return history_list[-1][:]
    else:
        return []

def add_to_list_history(history_list:list[list[dict[str, int]]], lista:list[dict[str, int]]):
    """
    Adauga in lista care mentine istoricul listei principale asupra careia facem operatii
    :param history_list: lista ce mentine istoricul
    :param lista: lista asupra careia se fac operatii
    :return: no return
    """
    if len(history_list) >= 1 and lista != history_list[-1]:
        history_list.append([i.copy() for i in lista])
    elif len(history_list) == 0:
        history_list.append(lista.copy())
    return history_list #pentru teste