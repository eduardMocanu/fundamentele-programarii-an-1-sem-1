class Lending_repo:

    def __init__(self):
        self.__loans = {}

    def get_loans(self):
        return self.__loans

    def add_loan_to_existing_client(self, film, client):
        self.__loans[client].append(film)

    def create_client(self, client):
        self.__loans[client] = []

    def remove_loan(self, film, client):
        self.__loans[client].remove(film)
