import unittest

from lab7_9.errors.ServiceError import ServiceError
from lab7_9.model.Film import Film
from lab7_9.validators.film_validator import Film_validator


class TestFilmValidator(unittest.TestCase):

    def setUp(self):
        self.validator = Film_validator()

    def test_verify_film(self):
        film = Film(1, "Title", "Description", "Gen")
        self.assertIsNone(self.validator.verify_film(film))

        with self.assertRaises(ServiceError):
            self.validator.verify_film(Film(1, "", "Desc", "Gen"))

        with self.assertRaises(ServiceError):
            self.validator.verify_film(Film(1, "Title", "", "Gen"))

        with self.assertRaises(ServiceError):
            self.validator.verify_film(Film(1, "Title", "Desc", ""))

        with self.assertRaises(ServiceError):
            self.validator.verify_film(Film(-5, "Title", "Desc", "Gen"))

        with self.assertRaises(ServiceError):
            self.validator.verify_film(None)

    def test_id_verificator(self):
        self.assertIsNone(self.validator.id_verificator(1))

        with self.assertRaises(ServiceError):
            self.validator.id_verificator(0)

        with self.assertRaises(ServiceError):
            self.validator.id_verificator(-10)

