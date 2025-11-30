from lab7_9.errors.RepoError import RepoError


class Films_repo:

    def __init__(self):
        self.__films = []

    def get_all_films(self):
        """
        Returnează o copie a listei tuturor filmelor din repository.
        """
        return list(self.__films)

    def add_film(self, film):
        """
        Adaugă un film în repository.

        Ridică RepoError dacă există deja un film cu același ID.
        """
        if self.find_film_by_id(film.get_id()):
            raise RepoError("Filmul cu acest ID deja exista")
        self.__films.append(film)

    def remove_film(self, film):
        """
        Șterge un film din repository.

        Ridică RepoError dacă filmul nu există.
        """
        if self.find_film_by_id(film.get_id()) is None:
            raise RepoError("Acest film nu exista")
        self.__films.remove(film)

    def modify_film(self, film_id_old, film_new):
        """
        Modifică un film existent identificat prin film_id_old cu valorile din film_new.
        """
        for i in self.__films:
            if i.get_id() == film_id_old:
                i.set_id(film_new.get_id())
                i.set_titlu(film_new.get_titlu())
                i.set_descriere(film_new.get_descriere())
                i.set_gen(film_new.get_gen())
                break

    def find_film_by_id(self, film_id):
        """
        Caută și returnează filmul cu ID-ul specificat.

        Returnează None dacă nu există un astfel de film.
        """
        for i in self.__films:
            if i.get_id() == film_id:
                return i
        return None