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
 • suma numerelor dintr-o subsecventă dată (se da poziția de început și
sfârșit).
 • Produsul numerelor dintr-o subsecventă dată (se da poziția de început
și sfârșit).
 • Tipărește lista sortată descrescător după partea imaginara
 • Filtrare parte reala prim – elimină din listă numerele complexe la care
partea reala este prim.
 • Filtrare modul – elimina din lista numerele complexe la care modulul
este <,= sau > decât un număr dat.

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
Implementare meniu optiunile: 1, 3, 4, 5
lab 5 -
 modularizare proiect
 6. Undo
• Reface ultima operație (lista de numere revine la numerele ce existau
înainte de ultima operație care a modificat lista) – Nu folosiți funcția
deepCopy
lab 6 -
"""
from tests import test_function
from view import *


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

def check_list_length(lista:list[dict[str, int]]) -> bool:
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
    list_history = []
    list_main = []
    while True:
        add_to_list_history(list_history, list_main)
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
                print_list_complex_number(list_main)
            elif option == 2:
                number = read_complex_number()
                index = read_index_to_add(list_main)
                list_main = add_number_complex_to_list(list_main, index, number)
                new_list_message()
                print_list_complex_number(list_main)
        elif menu_option == 6:
            list_main = get_list_before_last_change(list_history)
            new_list_message()
            print_list_complex_number(list_main)
        elif middleware_functions_list(elemente_citite):
            if menu_option == 2:
                print_menu_option_2()
                option = menu_interact(3)
                if option == 0:
                    break
                elif option == 1:
                    index_to_remove = read_index_to_remove_item(list_main)
                    list_main = remove_element_on_index(list_main, index_to_remove)
                    new_list_message()
                    print_list_complex_number(list_main)
                elif option == 2:
                    indexes_to_remove = read_2_indexes_start_end(list_main)
                    list_main = remove_elements_subsequence(list_main, indexes_to_remove[0], indexes_to_remove[1])
                    new_list_message()
                    print_list_complex_number(list_main)
                elif option == 3:
                    print("Introdu numarul pe care doresti sa il inlocuiesti")
                    complex_number_to_be_replaced = read_complex_number()
                    print("Introdu numarul cu care doresti sa inlocuiesti")
                    complex_number_to_replace = read_complex_number()
                    list_main = replace_complex_value_with_another_one(list_main, complex_number_to_be_replaced, complex_number_to_replace)
                    new_list_message()
                    print_list_complex_number(list_main)
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
                    print_list_complex_number(get_sorted_list_by_imaginary_part(list_main))
            elif menu_option == 5:
                print_menu_option_5()
                option = menu_interact(2)
                if option == 0:
                    break
                elif option == 1:
                    list_main = remove_prime_real_part(list_main)[:]
                    new_list_message()
                    print_list_complex_number(list_main)
                elif option == 2:
                    print_submenu_option_5()
                    submenu = menu_interact(3)
                    print("Numarul cu care doresti sa compari este: ")
                    number = read_whole_number()
                    list_main = remove_elements_where_abs_value_doesnt_satisfy_request(list_main, submenu, number)[:]
                    new_list_message()
                    print_list_complex_number(list_main)



    print("bye bye")

test_function()
main()
