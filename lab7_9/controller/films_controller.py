from lab7_9.Validators import Validators
from lab7_9.model.Film import Film
from lab7_9.service.films_service import Films_service


class Films_controller:

    def __init__(self, films_service:Films_service, validator:Validators):
        self.__films_service = films_service
        self.__validators = validator

    def add_film(self, film_id, film_title, film_descriere, film_gen):
        if not self.__validators.check_int(film_id):
            return "Id-ul introdus este invalid"
        try:
            return self.__films_service.add_film(Film(int(film_id), film_title, film_descriere, film_gen))
        except ValueError as e:
            return str(e)

    def remove_film(self, film_id):
        if not self.__validators.check_int(film_id):
            return "Id-ul introdus este invalid"
        try:
            return self.__films_service.remove_film(int(film_id))
        except ValueError as e:
            return str(e)

    def modify_film(self, film_id_old, film_id_new, film_title_new, film_descriere_new, film_gen_new):
        if not self.__validators.check_int(film_id_old):
            return "id-ul vechi al filmului este invalid"
        if not self.__validators.check_int(film_id_new):
            return "id-ul nou al filmului este invalid"
        try:
            return self.__films_service.modify_film(int(film_id_new), Film(int(film_id_new), film_title_new, film_descriere_new, film_gen_new))
        except ValueError as e:
            return str(e)