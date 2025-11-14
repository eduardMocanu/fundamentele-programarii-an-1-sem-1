from lab7_9.model.Film import Film


class Films_service:
    def __init__(self, films_repo, validator_film):
        self.__films_repo = films_repo
        self.__film_validator = validator_film

    def add_film(self, film_id, film_title, film_description, film_gen):
        """
        Creează și validează un film nou, apoi îl adaugă în repository.

        Ridică ServiceError dacă filmul nu trece validările.
        """
        film = Film(film_id, film_title, film_description, film_gen)
        self.__film_validator.verify_film(film)
        self.__films_repo.add_film(film)

    def remove_film_by_id(self, film_id):
        """
        Verifică ID-ul și șterge filmul corespunzător din repository.

        Ridică ServiceError dacă ID-ul este invalid sau filmul nu există.
        """
        self.__film_validator.id_verificator(film_id)
        film = self.__films_repo.find_film_by_id(film_id)
        self.__film_validator.verify_film(film)
        self.__films_repo.remove_film(film)

    def modify_film(self, film_id_old, film_id_new, film_title_new, film_description_new, film_gen_new):
        """
        Modifică un film existent cu noile valori furnizate.

        Ridică ServiceError dacă filmul vechi nu există sau noul film nu este valid.
        """
        film_new = Film(film_id_new, film_title_new, film_description_new, film_gen_new)
        self.__film_validator.verify_film(film_new)
        film_old = self.__films_repo.find_film_by_id(film_id_old)
        self.__film_validator.verify_film(film_old)
        self.__films_repo.modify_film(film_id_old, film_new)

    def search_film_by_id(self, film_id):
        """
        Caută un film după ID și îl returnează.

        Ridică ServiceError dacă ID-ul este invalid sau nu există filmul.
        """
        self.__film_validator.id_verificator(film_id)
        film = self.__films_repo.find_film_by_id(film_id)
        self.__film_validator.verify_film(film)
        return film

    def get_films(self):
        """
        Returnează lista tuturor filmelor din repository.
        """
        return self.__films_repo.get_all_films()