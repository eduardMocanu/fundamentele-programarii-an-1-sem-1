from lab7_9.errors.RepoError import RepoError


class Loans_repo:

    def __init__(self):
        self.__loans = {}

    def get_loans(self):
        """
        Returnează toate împrumuturile din repository.

        Returns:
            dict: Dicționar cu mapping între client_id și lista de film_id-uri împrumutate.
        """
        return self.__loans

    def add_loan(self, client_id, film_id):
        """
        Adaugă un împrumut între un client și un film.

        Dacă clientul nu există în dicționar, este adăugat automat.
        Dacă filmul este deja împrumutat de client, se aruncă o eroare.

        Args:
            client_id (int): ID-ul clientului.
            film_id (int): ID-ul filmului care se împrumută.

        Raises:
            RepoError: Dacă filmul este deja împrumutat de același client.
        """
        if client_id in self.__loans:
            if film_id not in self.__loans[client_id]:
                self.__loans[client_id].append(film_id)
            else:
                raise RepoError("Acest client a inchiriat deja acest film")
        else:
            self.__loans[client_id] = [film_id]

    def remove_loan(self, client_id, film_id):
        """
        Elimină un împrumut existent între un client și un film.

        Args:
            client_id (int): ID-ul clientului.
            film_id (int): ID-ul filmului ce urmează să fie restituit.

        Raises:
            RepoError:
                - Dacă clientul nu există în repository.
                - Dacă filmul nu se află în lista de împrumuturi a acelui client.
        """
        if client_id not in self.__loans:
            raise RepoError("Acest client nu exista in baza de date cu inchirieri")

        if film_id not in self.__loans[client_id]:
            raise RepoError("Acest client nu are filmul dat inchiriat")

        self.__loans[client_id].remove(film_id)