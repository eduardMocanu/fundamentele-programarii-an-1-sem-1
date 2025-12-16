from lab7_9.errors.RepoError import RepoError
from lab7_9.model.Film import Film


class Films_repo:

    def __init__(self, file_db = "/Users/eduardmocanu/School/fundamentele programarii sem 1 an 1/lab7_9/db/films.txt"):
        self.__films = []
        self.__db_films = file_db

    def get_films(self):
        return list(self.__films)

    def get_all_films(self):
        """
        Returnează o copie a listei tuturor filmelor din repository.
        """
        self.read_all_films()
        return list(self.__films)

    def add_film(self, film):
        """
        Adaugă un film în repository.

        Ridică RepoError dacă există deja un film cu același ID.
        """
        self.read_all_films()
        if self.find_film_by_id(film.get_id()):
            raise RepoError("Filmul cu acest ID deja exista")
        self.__films.append(film)
        self.write_all_films()

    def remove_film(self, film):
        """
        Șterge un film din repository.

        Ridică RepoError dacă filmul nu există.
        """
        self.read_all_films()
        if self.find_film_by_id(film.get_id()) is None:
            raise RepoError("Acest film nu exista")
        self.__films.remove(film)
        self.write_all_films()


    def modify_film(self, film_id_old, film_new):
        """
        Modifică un film existent identificat prin film_id_old cu valorile din film_new.
        """
        self.read_all_films()
        for i in self.__films:
            if i.get_id() == film_id_old:
                i.set_id(film_new.get_id())
                i.set_titlu(film_new.get_titlu())
                i.set_descriere(film_new.get_descriere())
                i.set_gen(film_new.get_gen())
                break
        self.write_all_films()

    def find_film_by_id(self, film_id, index = 0):
        """
        Caută și returnează filmul cu ID-ul specificat.

        Returnează None dacă nu există un astfel de film.

        Recursiv
        """
        if index == 0:
            self.read_all_films()
        if index == len(self.get_films()):
            return None
        film = self.get_films()[index]
        if film_id == film.get_id():
            return film
        return self.find_film_by_id(film_id, index + 1)

    def set_films(self, films):
        self.__films = films

    def read_all_films(self):
        with open(self.__db_films, "r") as f:
            lines = f.readlines()
            films = []
            for line in lines:
                if line == "":
                    break
                parts = line.split(",")
                film_id = int(parts[0])
                film_title = parts[1].strip()
                film_description = parts[2].strip()
                film_gen = parts[3].strip()
                film = Film(film_id, film_title, film_description, film_gen)
                films.append(film)
            self.set_films(films)

    def write_all_films(self):
        with open(self.__db_films, "w") as f:
            for film in self.__films:
                film_id = film.get_id()
                film_title = film.get_titlu()
                film_description = film.get_descriere()
                film_gen = film.get_gen()
                f.write(f"{film_id},{film_title},{film_description},{film_gen}\n")
