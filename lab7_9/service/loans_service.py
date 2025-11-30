from lab7_9.repository.in_memory.loans_repo import Loans_repo
from lab7_9.service.clients_service import Clients_service
from lab7_9.service.films_service import Films_service


class Lending_service:

    def __init__(self, loan_repo: Loans_repo, clients_service: Clients_service, films_service: Films_service):

        self.__loan_repo = loan_repo
        self.__clients_service = clients_service
        self.__films_service = films_service

    def add_loan(self, client_id, film_id):
        """
        Creează un nou împrumut între un client și un film.

        Pași:
        - verifică dacă clientul există (altfel se aruncă eroare din service)
        - verifică dacă filmul există
        - adaugă împrumutul în repository

        Args:
            client_id (int): ID-ul clientului.
            film_id (int): ID-ul filmului.

        Raises:
            RepoError, ServiceError, UiError: dacă apar probleme la nivel de repo sau servicii.
        """
        self.__clients_service.search_client_by_id(client_id)
        self.__films_service.search_film_by_id(film_id)
        self.__loan_repo.add_loan(client_id, film_id)

    def remove_loan(self, client_id, film_id):
        """
        Elimină un împrumut existent (clientul returnează filmul).

        Pași:
        - verifică dacă clientul există
        - verifică dacă filmul există
        - elimină împrumutul din repository

        Args:
            client_id (int): ID-ul clientului.
            film_id (int): ID-ul filmului.

        Raises:
            RepoError, ServiceError, UiError: dacă împrumutul nu poate fi șters.
        """
        self.__clients_service.search_client_by_id(client_id)
        self.__films_service.search_film_by_id(film_id)
        self.__loan_repo.remove_loan(client_id, film_id)

    def clients_loaned_films_sorted(self):
        """
        Returnează lista clienților cu numărul lor de împrumuturi, ordonată alfabetic după nume.

        Returns:
            list[list]: Liste de forma [nume_client, numar_inchirieri].
        """
        loans = self.__loan_repo.get_loans()
        result = []
        for key, value in loans.items():
            nume = self.__clients_service.search_client_by_id(key).get_nume()
            number_of_loans = len(value)
            result.append([nume, number_of_loans])

        result.sort(key=lambda pair: pair[0])
        return result

    def most_loaned_films(self):
        """
        Returnează lista filmelor cu cel mai mare număr de împrumuturi.

        Dacă mai multe filme au același număr maxim, sunt returnate toate.

        Returns:
            list[Film]: Obiectele film corespunzătoare maximului de împrumuturi.

        Raises:
            ValueError: dacă nu există împrumuturi în sistem.
        """
        loans = self.__loan_repo.get_loans()
        films = {}

        for values in loans.values():
            for film_id in values:
                films[film_id] = films.get(film_id, 0) + 1
        if len(films) == 0:
            return []
        maximum = max(films.values())

        result = []
        for film_id, count in films.items():
            if count == maximum:
                result.append(self.__films_service.search_film_by_id(film_id))

        return result

    def top_30_clients(self):
        """
        Returnează top 30% dintre clienți în funcție de numărul de filme împrumutate,
        ordonați descrescător.

        Calcul:
            top_size = total_clienti // 3

        Returns:
            list[list]: Liste de forma [nume_client, numar_inchirieri].
        """
        number_of_clients_in_top = len(self.__clients_service.get_clients()) // 3
        loans = self.__loan_repo.get_loans()

        all_clients_number_of_loaned_films = []
        for client_id, films in loans.items():
            nume = self.__clients_service.search_client_by_id(client_id).get_nume()
            number_of_loans = len(films)
            all_clients_number_of_loaned_films.append([nume, number_of_loans])

        all_clients_number_of_loaned_films.sort(key=lambda pair: pair[1], reverse=True)

        return all_clients_number_of_loaned_films[:number_of_clients_in_top]

    def __top_x_clients(self, x):
        loans = self.__loan_repo.get_loans()
        clients_list = []
        for i in loans:
            clients_list.append([i, len(loans[i])])
        clients_list.sort(key = lambda item: item[1], reverse = True)
        lista_doar_id = [i[0] for i in clients_list]
        if x > len(clients_list):
            return lista_doar_id
        return lista_doar_id[:x]

    def __top_x_films(self, x):
        loans = self.__loan_repo.get_loans()
        films_dict = {}
        for i in loans:
            for item in loans[i]:
                if item not in films_dict:
                    films_dict[item] = 0
                films_dict[item] += 1
        films_list = []
        for i in films_dict:
            films_list.append([i, films_dict[i]])
        films_list.sort(key = lambda item: item[1], reverse=True)
        lista_doar_id = [i[0] for i in films_list]
        if x > len(films_list):
            return films_list
        return lista_doar_id[:x]

    def top_x_combined(self, x):
        top_clients = self.__top_x_clients(x)
        top_films = self.__top_x_films(x)
        loans = self.__loan_repo.get_loans()
        top_merged = {}
        for i in loans:
            if i in top_clients:
                top_merged[i] = []
                for j in loans[i]:
                    if j in top_films:
                        top_merged[i].append(j)
        top_nume = {}
        for i in top_merged:
            nume_client = self.__clients_service.search_client_by_id(i).get_nume()
            top_nume[nume_client] = []
            for j in top_merged[i]:
                top_nume[nume_client].append(self.__films_service.search_film_by_id(j))
        return top_nume
