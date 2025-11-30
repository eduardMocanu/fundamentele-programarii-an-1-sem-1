import unittest

from lab7_9.service.films_service import Films_service
from lab7_9.errors.ServiceError import ServiceError
from lab7_9.repository.in_memory.films_repo import Films_repo
from lab7_9.validators.film_validator import Film_validator


class TestFilmsService(unittest.TestCase):

    def setUp(self):
        self.repo = Films_repo()
        self.validator = Film_validator()
        self.service = Films_service(self.repo, self.validator)

    def test_add_film(self):
        with self.assertRaises(ServiceError):
            self.service.add_film(1, "", "Desc", "Gen")

        self.service.add_film(1, "Title", "Desc", "Gen")
        films = self.service.get_films()

        self.assertTrue(any(f.get_id() == 1 and f.get_titlu() == "Title" for f in films))

    def test_remove_film_by_id(self):
        self.service.add_film(1, "Test", "Desc", "Gen")
        self.service.remove_film_by_id(1)

        self.assertTrue(all(f.get_id() != 1 for f in self.service.get_films()))

        with self.assertRaises(ServiceError):
            self.service.remove_film_by_id(999)

    def test_modify_film(self):
        self.service.add_film(1, "Old", "OldDesc", "OldGen")
        self.service.modify_film(1, 2, "New", "NewDesc", "NewGen")

        films = self.service.get_films()
        modified = next((f for f in films if f.get_id() == 2), None)

        self.assertIsNotNone(modified)
        self.assertEqual(modified.get_titlu(), "New")
        self.assertEqual(modified.get_descriere(), "NewDesc")
        self.assertEqual(modified.get_gen(), "NewGen")

        with self.assertRaises(ServiceError):
            self.service.modify_film(999, 10, "X", "Y", "Z")

    def test_search_film_by_id(self):
        self.service.add_film(10, "Movie", "Desc", "Gen")

        found = self.service.search_film_by_id(10)

        self.assertEqual(found.get_id(), 10)
        self.assertEqual(found.get_titlu(), "Movie")
        self.assertEqual(found.get_descriere(), "Desc")

        with self.assertRaises(ServiceError):
            self.service.search_film_by_id(999)

    def test_get_films(self):
        self.assertEqual(self.service.get_films(), [])

        self.service.add_film(1, "A", "D1", "G1")
        self.service.add_film(2, "B", "D2", "G2")

        films = self.service.get_films()

        self.assertTrue(any(f.get_id() == 1 for f in films))
        self.assertTrue(any(f.get_id() == 2 for f in films))
        self.assertEqual(len(films), 2)

