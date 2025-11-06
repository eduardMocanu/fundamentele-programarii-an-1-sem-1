from lab7_9.repository.lending_repo import Lending_repo


class Loan_service:

    def __init__(self, loan_repo:Lending_repo):
        self.__loan_repo = loan_repo

    def add_loan(self, film, client):
        return self.__loan_repo.add_loan(film, client)

    def remove_loan(self, film, client):
        return self.__loan_repo.remove_loan(film, client)

    def get_loans(self):
        return self.__loan_repo.get_loans()