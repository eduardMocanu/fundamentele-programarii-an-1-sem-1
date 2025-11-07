from lab7_9.repository.lending_repo import Lending_repo


class Lending_service:

    def __init__(self, loan_repo:Lending_repo):
        self.__loan_repo = loan_repo

    def add_loan(self, film, client):
        loans = self.__loan_repo.get_loans()
        if not(client in loans.keys()):
            self.__loan_repo.create_client(client)
        if film in loans[client]:
            raise ValueError("Acest client a imprumutat deja acest film")
        else:
            self.__loan_repo.add_loan_to_existing_client(film, client)

    def remove_loan(self, film, client):
        loans = self.__loan_repo.get_loans()
        if client in loans and film in loans[client]:
            self.__loan_repo.remove_loan(film, client)
        raise ValueError("Nu exista un imprumut valid")

    def get_loans(self):
        return self.__loan_repo.get_loans()