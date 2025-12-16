import unittest

from test_simulare_acasa.model.Student import Student
from test_simulare_acasa.repository.students_repo import Students_repo
from test_simulare_acasa.service.students_service import Students_service


class Test_students_service(unittest.TestCase):
    __test_db = "/Users/eduardmocanu/School/fundamentele programarii sem 1 an 1/test_simulare_acasa/tests/test_db/students.txt"
    students_service = Students_service(Students_repo(__test_db))



    def setUp(self):
        self.helper_add_data()

    def tearDown(self):
        with open(self.__test_db, "w") as f:
            pass

    def helper_add_data(self):
        with open(self.__test_db, "w") as f:
            f.write("1,1\n")
            f.write("2,2\n")

    def test_add_student(self):
        self.students_service.add_student(3, "3")
        students = self.students_service.get_all_students()
        self.assertIn(Student(3, "3"), students.values(), "Not added properly")

    def test_remove_student(self):
        self.students_service.remove_student(1)
        students = self.students_service.get_all_students()
        self.assertNotIn(Student(1, "1"), students.values())

    def test_modify_student(self):
        self.students_service.modify_student(5, "5", 1)
        students = self.students_service.get_all_students()
        self.assertIn(Student(5, "5"), students.values())
        self.assertNotIn(Student(1, "1"), students.values())

    def test_get_all_students(self):
        students = self.students_service.get_all_students()
        self.assertIn(Student(1, "1"), students.values())
        self.assertIn(Student(2, "2"), students.values())