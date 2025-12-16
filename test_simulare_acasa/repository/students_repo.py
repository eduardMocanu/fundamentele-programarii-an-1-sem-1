from test_simulare_acasa.errors.repo_error import Repo_error
from test_simulare_acasa.model.Student import Student


class Students_repo:

    def __init__(self, students_db_file_name = "/Users/eduardmocanu/School/fundamentele programarii sem 1 an 1/test_simulare_acasa/db/students.txt"):
        self.__students = {}
        self.__db_file = students_db_file_name

    def set_students(self, students):
        self.__students = students

    def __read_all_students(self):
        with open(self.__db_file, "r") as f:
            lines = f.readlines()
            students = {}
            for line in lines:
                line = line.strip()
                if not line:
                    break
                parts = line.split(",")
                studentId = int(parts[0])
                studentName = parts[1]
                student = Student(studentId, studentName)
                students[student.get_id()] = student
        self.set_students(students)

    def __write_all_students(self):
        with open(self.__db_file, "w") as f:
            for student in self.__students:
                line = f"{student},{self.__students[student].get_name()}\n"
                f.write(line)

    def get_all_students(self):
        self.__read_all_students()
        return self.__students

    def add_student(self, student:Student):
        self.__read_all_students()
        if student.get_id() in self.__students:
            raise Repo_error("Acest id exista deja in baza de date")
        self.__students[student.get_id()] = student
        self.__write_all_students()

    def remove_student(self, student_id):
        self.__read_all_students()
        if student_id in self.__students:
            self.__students.pop(student_id)
        self.__write_all_students()

    def modify_student(self, student:Student, student_id_old):
        self.__read_all_students()
        if student_id_old not in self.__students:
            raise Repo_error("Acest id nu exista in baza de date cu studenti")
        self.__students.pop(student_id_old)
        self.__students[student.get_id()] = student
        self.__write_all_students()
