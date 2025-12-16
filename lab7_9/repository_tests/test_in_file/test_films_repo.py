import unittest
from lab7_9.model.Film import Film
from lab7_9.repository.in_file.films_repo import Films_repo


class TestFilmsRepo(unittest.TestCase):


    file_db_films = "/Users/eduardmocanu/School/fundamentele programarii sem 1 an 1/lab7_9/repository_tests/test_in_file/test_db/test_films.txt"
    repo = Films_repo(file_db_films)

    def setUp(self):
        self.helper_add_data()
        self.repo = Films_repo(self.file_db_films)

    def tearDown(self):
        with open(self.file_db_films, "w") as f:
            pass

    def helper_add_data(self):
        with open(self.file_db_films, "w") as f:
            f.writelines(["1,Title,Desc,Gen\n", "2,E,desc,g\n", "3,4314,314,41324\n", "4,42134,314,4345\n"])


    def test_add_film(self):
        film = Film(100, "Title", "Desc", "Gen")
        self.repo.add_film(film)
        self.assertIn(film, self.repo.get_all_films())

    def test_remove_film(self):
        film = Film(100, "Title", "Desc", "Gen")
        self.repo.add_film(film)
        self.repo.remove_film(film)
        self.assertNotIn(film, self.repo.get_all_films())

    def test_modify_film(self):
        old_film = Film(1, "Title", "Desc", "Gen")

        new_film = Film(100, "NewTitle", "NewDesc", "NewGen")
        self.repo.modify_film(old_film.get_id(), new_film)

        modified = self.repo.find_film_by_id(100)

        self.assertIsNotNone(modified)
        self.assertEqual(modified.get_titlu(), "NewTitle")
        self.assertEqual(modified.get_descriere(), "NewDesc")
        self.assertEqual(modified.get_gen(), "NewGen")

    def test_find_film_by_id(self):

        self.assertEqual(self.repo.find_film_by_id(1), Film(1, "Title", "Desc", "Gen"))
        self.assertIsNone(self.repo.find_film_by_id(99))

    def test_get_all_films(self):
        f1 = Film(101, "Title", "Desc", "Gen")
        f2 = Film(100, "E", "desc", "g")
        self.repo.add_film(f1)
        self.repo.add_film(f2)

        films = self.repo.get_all_films()

        self.assertIn(f1, films)
        self.assertIn(f2, films)


