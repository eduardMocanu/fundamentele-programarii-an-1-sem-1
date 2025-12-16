from test_simulare_acasa.errors.service_error import Service_error
from test_simulare_acasa.model.Student import Student


class Students_validators:

    def __init__(self):
        pass

    def validate_student(self, student:Student):
        if student is None:
            raise Service_error("Student invalid")
        if student.get_id() < 0:
            raise Service_error("Id negativ")
        if len(student.get_name()) == 0:
            raise Service_error("Nume gol")

    def validate_student_id(self, student_id):
        if student_id < 0:
            raise Service_error("Id negativ")