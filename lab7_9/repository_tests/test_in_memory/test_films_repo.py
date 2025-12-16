import unittest
from lab7_9.model.Film import Film
from lab7_9.repository.in_memory.films_repo import Films_repo


class TestFilmsRepo(unittest.TestCase):

    def test_add_film(self):
        repo = Films_repo()
        film = Film(1, "Title", "Desc", "Gen")
        repo.add_film(film)
        self.assertIn(film, repo.get_all_films())

    def test_remove_film(self):
        repo = Films_repo()
        film = Film(1, "Title", "Desc", "Gen")
        repo.add_film(film)
        repo.remove_film(film)
        self.assertNotIn(film, repo.get_all_films())

    def test_modify_film(self):
        repo = Films_repo()
        old_film = Film(1, "OldTitle", "OldDesc", "OldGen")
        repo.add_film(old_film)

        new_film = Film(2, "NewTitle", "NewDesc", "NewGen")
        repo.modify_film(old_film.get_id(), new_film)

        modified = repo.find_film_by_id(2)

        self.assertIsNotNone(modified)
        self.assertEqual(modified.get_titlu(), "NewTitle")
        self.assertEqual(modified.get_descriere(), "NewDesc")
        self.assertEqual(modified.get_gen(), "NewGen")

    def test_find_film_by_id(self):
        repo = Films_repo()
        film = Film(10, "ABC", "DEF", "XYZ")
        repo.add_film(film)

        self.assertEqual(repo.find_film_by_id(10), film)
        self.assertIsNone(repo.find_film_by_id(99))

    def test_get_all_films(self):
        repo = Films_repo()
        f1 = Film(1, "T1", "D1", "G1")
        f2 = Film(2, "T2", "D2", "G2")
        repo.add_film(f1)
        repo.add_film(f2)

        films = repo.get_all_films()

        self.assertIn(f1, films)
        self.assertIn(f2, films)


