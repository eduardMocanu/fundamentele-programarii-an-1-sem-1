class Films_service:
    def __init__(self, films_repo):
        self.__films_repo = films_repo

    def add_film(self, film):
        existing = self.__films_repo.search_film_by_id(film.get_id())
        if existing is not None:
            raise ValueError("Exista deja un film cu acest ID.")
        self.__films_repo.add_film(film)

    def remove_film(self, film_id):
        film = self.__films_repo.search_film_by_id(film_id)
        if film is None:
            raise ValueError("Nu exista un film cu acest ID.")
        self.__films_repo.remove_film(film)

    def modify_film(self, film_id_old, film_new):
        film = self.__films_repo.search_film_by_id(film_id_old)
        if film is None:
            raise ValueError("Nu exista un film cu acest ID.")
        if film_id_old != film_new.get_id():
            if self.__films_repo.search_film_by_id(film_new.get_id()) is not None:
                raise ValueError("Exista deja un film cu noul ID.")
        self.__films_repo.modify_film(film_id_old, film_new)

    def search_film_by_id(self, film_id):
        film = self.__films_repo.search_film_by_id(film_id)
        if film is None:
            raise ValueError("Nu exista un film cu acest ID.")
        return film

    def get_films(self):
        return self.__films_repo.get_films()