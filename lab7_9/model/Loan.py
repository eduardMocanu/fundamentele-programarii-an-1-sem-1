class Loan:
    def __init__(self, film_id, client_id):
        self.__film_id = film_id
        self.__client_id = client_id

    def get_film_id(self):
        return self.__film_id

    def get_client_id(self):
        return self.__client_id
