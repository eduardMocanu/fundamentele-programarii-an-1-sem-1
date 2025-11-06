from test_partial.Film import Film


class Film_service:
    def __init__(self, repo, validators):
        self.repo = repo
        self.validators = validators

    def adauga_film(self, ID, titlu, descriere, nr_stele):
        if not self.validators.check_ID(ID):
            return "ID invalid"
        return self.repo.add_film(Film(ID, titlu, descriere, nr_stele))

    def sterge_film(self, ID):
        if not self.validators.check_ID(ID):
            return "ID invalid"
        return self.repo.sterge_film(ID)

    def modifica_film(self, ID, ID_nou, titlu_nou, descriere_nou, nr_stele_nou):
        if not self.validators.check_ID(ID):
            return "ID invalid"
        elif not self.validators.check_ID(ID_nou):
            return "ID nou invalid"
        return self.repo.modifica_film(ID, ID_nou, titlu_nou, descriere_nou, nr_stele_nou)

    def get_films(self):
        return self.repo.filme