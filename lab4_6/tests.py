from controller import *


def test_prime_number():
    """
    Testeaza functionalitatea corecta a functiei prime_number
    :return: no return
    """
    assert prime_number(1) == False
    assert prime_number(2) == True
    assert prime_number(3) == True
    assert prime_number(4) == False

def test_add_number_complex_to_list():
    """
    Testează funcționalitatea funcției add_number_complex_to_list.
    """
    l1 = [create_complex_number(1, 2), create_complex_number(3, 4)]
    expected = [create_complex_number(1, 2), create_complex_number(3, 4), create_complex_number(5, 6)]
    assert add_number_complex_to_list(l1.copy(), -1, create_complex_number(5, 6)) == expected

    l2 = [create_complex_number(1, 2), create_complex_number(3, 4)]
    expected = [create_complex_number(5, 6), create_complex_number(1, 2), create_complex_number(3, 4)]
    assert add_number_complex_to_list(l2.copy(), 0, create_complex_number(5, 6)) == expected

    l3 = [create_complex_number(1, 2), create_complex_number(3, 4)]
    expected = [create_complex_number(1, 2), create_complex_number(5, 6), create_complex_number(3, 4)]
    assert add_number_complex_to_list(l3.copy(), 1, create_complex_number(5, 6)) == expected

def test_remove_element_on_index():
    """
    Testează funcționalitatea corectă a funcției remove_element_on_index.
    """
    l1 = [create_complex_number(1, 2), create_complex_number(3, 4)]
    expected = [create_complex_number(3, 4)]
    assert remove_element_on_index(l1, 0) == expected

    l2 = [create_complex_number(1, 2), create_complex_number(3, 4), create_complex_number(5, 6)]
    expected = [create_complex_number(1, 2), create_complex_number(5, 6)]
    assert remove_element_on_index(l2, 1) == expected

    l3 = [create_complex_number(1, 2), create_complex_number(3, 4), create_complex_number(5, 6)]
    expected = [create_complex_number(1, 2), create_complex_number(3, 4)]
    assert remove_element_on_index(l3, 2) == expected

def test_remove_elements_subsequence():
    """
    Testează funcționalitatea corectă a funcției remove_elements_subsequence.
    """
    l1 = [create_complex_number(1, 2), create_complex_number(2, 3)]
    expected = []
    assert remove_elements_subsequence(l1, 0, 1) == expected

    l2 = [create_complex_number(1, 2), create_complex_number(2, 3), create_complex_number(4, 5)]
    expected = [create_complex_number(4, 5)]
    assert remove_elements_subsequence(l2, 0, 1) == expected

    l3 = []
    expected = []
    assert remove_elements_subsequence(l3, 10, 11) == expected

def test_replace_complex_value_with_another_one():
    """
    Testează funcționalitatea corectă a funcției replace_complex_value_with_another_one.
    """
    l1 = [create_complex_number(1, 2), create_complex_number(3, 4)]
    expected = [create_complex_number(10, 11), create_complex_number(3, 4)]
    assert replace_complex_value_with_another_one(
        l1,
        create_complex_number(1, 2),
        create_complex_number(10, 11)
    ) == expected

    l2 = [
        create_complex_number(1, 2),
        create_complex_number(3, 4),
        create_complex_number(5, 6),
        create_complex_number(5, 6),
        create_complex_number(5, 6)
    ]
    expected = [
        create_complex_number(1, 2),
        create_complex_number(3, 4),
        create_complex_number(1, 4),
        create_complex_number(1, 4),
        create_complex_number(1, 4)
    ]
    assert replace_complex_value_with_another_one(
        l2,
        create_complex_number(5, 6),
        create_complex_number(1, 4)
    ) == expected

    l3 = []
    expected = []
    assert replace_complex_value_with_another_one(
        l3,
        create_complex_number(5, 6),
        create_complex_number(1, 4)
    ) == expected


def test_get_all_imaginary_numbers_where_abs_value_less_than_10():
    """
    Testează funcționalitatea corectă a funcției
    get_all_imaginary_numbers_where_abs_value_less_than_10.
    """
    l1 = [create_complex_number(1, 2), create_complex_number(6, 7)]
    expected = [create_complex_number(1, 2), create_complex_number(6, 7)]
    assert get_all_imaginary_numbers_where_abs_value_less_than_10(l1) == expected

    l2 = [create_complex_number(1, 2), create_complex_number(100, 101)]
    expected = [create_complex_number(1, 2)]
    assert get_all_imaginary_numbers_where_abs_value_less_than_10(l2) == expected

    l3 = []
    expected = []
    assert get_all_imaginary_numbers_where_abs_value_less_than_10(l3) == expected

def test_get_all_imaginary_numbers_where_abs_value_equals_10():
    """
    Testează funcționalitatea corectă a funcției
    get_all_imaginary_numbers_where_abs_value_equals_10.
    """
    l1 = [create_complex_number(1, 2), create_complex_number(6, 8)]
    expected = [create_complex_number(6, 8)]
    assert get_all_imaginary_numbers_where_abs_value_equals_10(l1) == expected

    l2 = [create_complex_number(1, 2), create_complex_number(100, 101)]
    expected = []
    assert get_all_imaginary_numbers_where_abs_value_equals_10(l2) == expected

    l3 = []
    expected = []
    assert get_all_imaginary_numbers_where_abs_value_equals_10(l3) == expected

def test_subsequence_sum():
    """
    Testează funcționalitatea corectă a funcției subsequence_sum.
    """
    l1 = [
        create_complex_number(1, 2),
        create_complex_number(3, 4),
        create_complex_number(5, 6),
    ]
    assert subsequence_sum(l1, 0, 2) == [9, 12]

    l2 = [
        create_complex_number(4, 5),
        create_complex_number(6, 7),
    ]
    assert subsequence_sum(l2, 0, 0) == [4, 5]

    l3 = []
    assert subsequence_sum(l3, 0, 100) == [0, 0]

def test_subsequence_product():
    """
    Testează funcționalitatea corectă a funcției subsequence_product.
    """
    l1 = [create_complex_number(2, 3)]
    assert subsequence_product(l1, 0, 0) == create_complex_number(2, 3)

    l2 = [
        create_complex_number(2, 3),
        create_complex_number(1, 1),
    ]
    assert subsequence_product(l2, 0, 1) == create_complex_number(-1, 5)

    l3 = [
        create_complex_number(1, 1),
        create_complex_number(2, 0),
        create_complex_number(0, 1),
    ]
    assert subsequence_product(l3, 0, 2) == create_complex_number(-2, 2)


def test_get_sorted_list_by_imaginary_part():
    """
    Testează funcționalitatea corectă a funcției get_sorted_list_by_imaginary_part.
    """
    l1 = [
        create_complex_number(1, 2),
        create_complex_number(3, 4),
        create_complex_number(1, 1)
    ]
    assert get_sorted_list_by_imaginary_part(l1) == [
        create_complex_number(3, 4),
        create_complex_number(1, 2),
        create_complex_number(1, 1)
    ]

    l2 = [
        create_complex_number(1, 1),
        create_complex_number(2, 2),
        create_complex_number(3, 3)
    ]
    assert get_sorted_list_by_imaginary_part(l2) == [
        create_complex_number(3, 3),
        create_complex_number(2, 2),
        create_complex_number(1, 1)
    ]

    assert get_sorted_list_by_imaginary_part([]) == []

def test_remove_prime_real_part():
    """
    Testează funcționalitatea corectă a funcției remove_prime_real_part.
    """
    l1 = [
        create_complex_number(1, 2),
        create_complex_number(3, 4),
        create_complex_number(4, 5)
    ]
    assert remove_prime_real_part(l1) == [
        create_complex_number(1, 2),
        create_complex_number(4, 5)
    ]

    l2 = [
        create_complex_number(4, 5),
        create_complex_number(6, 7),
        create_complex_number(8, 9)
    ]
    assert remove_prime_real_part(l2) == [
        create_complex_number(4, 5),
        create_complex_number(6, 7),
        create_complex_number(8, 9)
    ]

    assert remove_prime_real_part([]) == []

def test_remove_elements_where_abs_value_doesnt_satisfy_request():
    """
    Testează funcționalitatea corectă a funcției remove_elements_where_abs_value_doesnt_satisfy_request.
    """
    data = [
        create_complex_number(3, 4),
        create_complex_number(1, 2),
        create_complex_number(0, 0),
        create_complex_number(5, 12)
    ]

    assert remove_elements_where_abs_value_doesnt_satisfy_request(data, 1, 5) == [
        create_complex_number(3, 4),
        create_complex_number(5, 12)
    ]
    assert remove_elements_where_abs_value_doesnt_satisfy_request(data, 2, 5) == [
        create_complex_number(1, 2),
        create_complex_number(0, 0),
        create_complex_number(5, 12)
    ]
    assert remove_elements_where_abs_value_doesnt_satisfy_request(data, 3, 5) == [
        create_complex_number(3, 4),
        create_complex_number(1, 2),
        create_complex_number(0, 0)
    ]
    assert remove_elements_where_abs_value_doesnt_satisfy_request([], 1, 5) == []
    assert remove_elements_where_abs_value_doesnt_satisfy_request(
        [create_complex_number(3, 4)], 3, 6
    ) == [create_complex_number(3, 4)]

def test_get_list_before_last_change():
    """
    Testeaza functionalitatea corecta a functiei get_list_before_last_change
    :return:
    """
    assert get_list_before_last_change([[], [create_complex_number(1, 2), create_complex_number(3, 4)]]) == []
    assert get_list_before_last_change([[]]) == []


def test_add_to_list_history():
    """
    Testeaza functionalitatea corecta a functiei add_to_list_history
    """
    assert add_to_list_history([[]], [create_complex_number(1, 2)]) == [[], [create_complex_number(1, 2)]]
    assert add_to_list_history([[], [create_complex_number(1, 2), create_complex_number(3, 4)]], [create_complex_number(1, 2), create_complex_number(3, 4)]) == [[], [create_complex_number(1, 2), create_complex_number(3, 4)]]





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
    test_get_list_before_last_change()
    test_add_to_list_history()

