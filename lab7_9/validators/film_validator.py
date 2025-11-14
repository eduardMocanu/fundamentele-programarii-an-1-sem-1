from lab7_9.errors.ServiceError import ServiceError

class Film_validator:

    def verify_film(self, film):
        """
        Verifică validitatea unui film.

        Ridică ServiceError dacă:
        - filmul este None
        - id-ul este <= 0
        - titlul este gol
        - descrierea este goală
        - genul este gol
        """
        if film is None:
            raise ServiceError("film invalid")
        if film.get_id() <= 0:
            raise ServiceError("id invalid")
        if len(film.get_titlu()) == 0:
            raise ServiceError("titlu invalid")
        if len(film.get_descriere()) == 0:
            raise ServiceError("descriere invalida")
        if len(film.get_gen()) == 0:
            raise ServiceError("gen invalid")

    def id_verificator(self, film_id):
        """
        Verifică validitatea unui ID de film.

        Ridică ServiceError dacă:
        - id-ul este <= 0
        """
        if film_id <= 0:
            raise ServiceError("id invalid")