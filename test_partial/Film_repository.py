class Film_repository:
    def __init__(self):
        self.filme = []

    def add_film(self, film):
        for i in self.filme:
            if i.ID == film.ID:
                return "exista un film cu acest ID"
        self.filme.append(film)
        return ""

    def sterge_film(self, ID):
        for i in self.filme:
            if i.ID == ID:
                self.filme.remove(i)
                return ""
        return "Nu exista un film cu acest ID"

    def modifica_film(self, ID, ID_nou, titlu, descriere, numar_stele):
        for i in self.filme:
            if i.ID == ID:
                i.ID = ID_nou
                i.titlu = titlu
                i.descriere = descriere
                i.numar_stele = numar_stele
                return ""
        return "nu exista un film cu acest ID"