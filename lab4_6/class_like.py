def get_real_part_complex_element(element:dict[str, int])->int:
    real_elem = element["real"]
    return real_elem

def get_imaginary_part_complex_element(element:dict[str, int])->int:
    imag_elem = element["imag"]
    return imag_elem

def set_real_part_complex_element(element:dict[str, int], value:int):
    element["real"] = value

def set_imag_part_complex_element(element:dict[str, int], value:int):
    element["imag"] = value

def create_complex_number(value_real:int, value_imag:int)->dict[str, int]:
    temp = {}
    temp["real"] = value_real
    temp["imag"] = value_imag
    return temp

