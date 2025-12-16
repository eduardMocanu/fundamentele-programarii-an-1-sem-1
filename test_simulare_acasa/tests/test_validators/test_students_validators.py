import unittest

from test_simulare_acasa.errors.service_error import Service_error
from test_simulare_acasa.model.Student import Student
from test_simulare_acasa.validators.students_validators import Students_validators


class Test_students_validators(unittest.TestCase):

    validator = Students_validators()

    def test_validate_student(self):
        student_good = Student(1, "1")
        student_bad = Student(-1, "4")

        self.assertIsNone(self.validator.validate_student(student_good))

        with self.assertRaises(Service_error):
            self.validator.validate_student(student_bad)

    def test_validate_student_id(self):
        student_id_good = 1
        student_id_bad = -1

        self.assertIsNone(self.validator.validate_student_id(student_id_good))
        with self.assertRaises(Service_error):
            self.validator.validate_student_id(student_id_bad)

