from lab7_9.repository.films_repo import Films_repo


class Films_service:

    def __init__(self, films_repo:Films_repo):
        self.__films_repo = films_repo

    def add_film(self, film):
        return self.__films_repo.add_film(film)

    def remove_film(self, film_id):
        return self.__films_repo.remove_film(film_id)

    def modify_film(self, film_id_old, film_new):
        return self.__films_repo.modify_film(film_id_old, film_new)

    def search_film_by_id(self, film_id):
        return self.__films_repo.search_film_by_id(film_id)

    def get_films(self):
        return self.__films_repo.get_films()