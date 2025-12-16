from test_simulare_acasa.model.Student import Student
from test_simulare_acasa.repository.students_repo import Students_repo
from test_simulare_acasa.validators.students_validators import Students_validators


class Students_service:

    def __init__(self, students_repo:Students_repo):
        self.__students_repo = students_repo
        self.__students_validator = Students_validators()

    def add_student(self, student_id, student_name):
        student = Student(student_id, student_name)
        self.__students_validator.validate_student(student)
        self.__students_repo.add_student(student)

    def remove_student(self, student_id):
        self.__students_validator.validate_student_id(student_id)
        self.__students_repo.remove_student(student_id)

    def modify_student(self, student_id, student_name, student_id_old):
        student = Student(student_id, student_name)
        self.__students_validator.validate_student(student)
        self.__students_repo.modify_student(student, student_id_old)

    def get_all_students(self):
        return self.__students_repo.get_all_students()