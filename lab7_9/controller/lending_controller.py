from lab7_9.Validators import Validators
from lab7_9.service.lending_service import Lending_service


class Lending_controller:

    def __init__(self, lending_service:Lending_service, validators:Validators):
        self.__lending_service = lending_service
        self.__validators = validators

    def sorted_client_loans(self):
        loans = self.__lending_service.get_loans()
        sorted_tuple = sorted(loans.items(), key= lambda item: (item[0].get_nume(), len(item[1])))
        return sorted_tuple

    def most_rented_films(self):
        loans = self.__lending_service.get_loans()
        film_rents = {}
        for i in loans.keys():
            for j in loans[i]:
                if j in film_rents:
                    film_rents[j] += 1
                else:
                    film_rents[j] = 1
        maximum = max(film_rents.values())
        maximum_number_rented_films = []
        for i in film_rents:
            if film_rents[i] == maximum:
                maximum_number_rented_films.append(i)
        return maximum_number_rented_films

    def top_30_clients(self):
        loans = self.__lending_service.get_loans()
        nr_clients_top= max(1, len(loans)//3)
        sorted_tuple = sorted(loans.items(), key = lambda item: len(item[1]), reverse=True)
        return sorted_tuple[:nr_clients_top]