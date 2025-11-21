class Film:

    def __init__(self, film_id, titlu, descriere, gen):
        self.__id = film_id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen

    def get_id(self):
        return self.__id

    def get_titlu(self):
        return self.__titlu

    def get_descriere(self):
        return self.__descriere

    def get_gen(self):
        return self.__gen

    def set_titlu(self, titlu):
        self.__titlu = titlu

    def set_descriere(self, descriere):
        self.__descriere = descriere

    def set_gen(self, gen):
        self.__gen = gen

    def set_id(self, film_id):
        self.__id = film_id

    def __repr__(self):
        return f"Titlu: {self.__titlu}, Descriere: {self.__descriere}, Gen: {self.__gen}"