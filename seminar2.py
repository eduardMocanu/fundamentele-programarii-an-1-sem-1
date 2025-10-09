def convert_str_to_int_list(s:str)->list:
    """
    Transforma un sir dat intr-o lista de numere
    :param s: sirul de transformat, preconditie: sir sub forma 1, 2, 3, 4
    :return: lista de numere obtinuta din sir, list
    """
    initial_list = s.split()
    numbers_list = []
    for i in range(len(initial_list)):
        numbers_list.append(int(initial_list[i]))
    return numbers_list

def read_list_ui():
    list_string = input("Introduceti lista: \n")
    list_of_nrs = convert_str_to_int_list(list_string)
    print(f"Lista curenta este: {list_of_nrs}")
    return list_of_nrs

def print_menu():
    print("1. Citire lista")
    print("2. Exit")

def run():
    list_of_numbers = []
    while True:
        print_menu()
        option = input("Introduceti optiunea: \n")
        if(option == "1"):
            list_of_numbers = read_list_ui()
        elif option == "2":
            break

run()

