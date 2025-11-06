class Lending_repo:

    def __init__(self):
        self.__loans = {}

    def get_loans(self):
        return self.__loans

    def add_loan(self, film, client):
        if client in self.__loans.keys():
            if film in self.__loans[client]:
                return "Clientul cu acest ID a imprumutat acest film deja"
            self.__loans[client].append(film)
        else:
            self.__loans[client] = [film]
        return ""

    def remove_loan(self, film, client):
        if client in self.__loans and film in self.__loans[client]:
            self.__loans[client].remove(film)
            if not self.__loans[client]:
                del self.__loans[client]
            return ""
        return "Nu exista un imprumut pentru acest film si acest client"
