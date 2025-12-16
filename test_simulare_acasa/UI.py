from test_simulare_acasa.errors.repo_error import Repo_error
from test_simulare_acasa.errors.service_error import Service_error
from test_simulare_acasa.service.students_service import Students_service


class UI:

    def __init__(self, students_service:Students_service, courses_service):
        self.__students_service = students_service
        self.__courses_service = courses_service

    def run(self):
        commands = {
            "add_student": self.add_student,
            "remove_student": self.remove_student,
            "modify_student": self.modify_student,
            "get_all_students": self.get_all_students
        }

        while True:
            command_whole = input("Introdu comanda: ").strip().lower()
            commands_parts = command_whole.split(" ")
            if len(commands_parts) > 1:
                print("Introdu o comanda valida")
                continue
            command = commands_parts[0].lower().strip()

            if command == "exit":
                break
            elif command in commands:
                commands[command]()
            else:
                print("Comanda invalida")
            print()


        print("bye")


    def add_student(self):
        try:
            student_id = int(input("Introdu id-ul studentului: "))
        except ValueError:
            print("Id invalid")
            return

        student_name = input("Introdu numele studentului: ")

        try:
            self.__students_service.add_student(student_id, student_name)
        except Service_error as e:
            print(e)
        except Repo_error as e:
            print(e)

    def remove_student(self):
        try:
            student_id = int(input("Introdu id-ul studentului: "))
        except ValueError:
            print("Id invalid")
            return

        try:
            self.__students_service.remove_student(student_id)
        except Service_error as e:
            print(e)
        except Repo_error as e:
            print(e)

    def modify_student(self):
        try:
            student_id = int(input("Introdu noul id al studentului: "))
        except ValueError:
            print("Id invalid")
            return

        student_name = input("Introdu noul nume al studentului: ")

        try:
            old_student_id = int(input("Introdu vechiul id al studentului: "))
        except ValueError:
            print("Id invalid")
            return

        try:
            self.__students_service.modify_student(student_id, student_name, old_student_id)
        except Service_error as e:
            print(e)
        except Repo_error as e:
            print(e)

    def get_all_students(self):
        students = self.__students_service.get_all_students()
        for student in students:
            print(students[student])

