class Films_repo:

    def __init__(self):
        self.__films = []

    def get_films(self):
        return self.__films

    def add_film(self, film):
        self.__films.append(film)

    def remove_film(self, film):
        self.__films.remove(film)

    def modify_film(self, film_id_old, film_new):
        for i in self.__films:
            if i.get_id() == film_id_old:
                i.set_id(film_new.get_id())
                i.set_titlu(film_new.get_titlu())
                i.set_descriere(film_new.get_descriere())
                i.set_gen(film_new.get_gen())
                break

    def search_film_by_id(self, film_id):
        for i in self.__films:
            if i.get_id() == film_id:
                return i
        return None

