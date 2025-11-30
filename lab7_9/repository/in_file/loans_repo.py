from lab7_9.errors.RepoError import RepoError


class Loans_repo:

    def __init__(self):
        self.__loans = {}
        self.__db_loans = "/Users/eduardmocanu/School/fundamentele programarii sem 1 an 1/lab7_9/db/loans.txt"

    def get_loans(self):
        """
        Returnează toate împrumuturile din repository.

        Returns:
            dict: Dicționar cu mapping între client_id și lista de film_id-uri împrumutate.
        """
        self.read_all_loans()
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
        self.read_all_loans()
        if client_id in self.__loans:
            if film_id not in self.__loans[client_id]:
                self.__loans[client_id].append(film_id)
            else:
                raise RepoError("Acest client a inchiriat deja acest film")
        else:
            self.__loans[client_id] = [film_id]
        self.write_all_loans()

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
        self.read_all_loans()
        if client_id not in self.__loans:
            raise RepoError("Acest client nu exista in baza de date cu inchirieri")

        if film_id not in self.__loans[client_id]:
            raise RepoError("Acest client nu are filmul dat inchiriat")

        self.__loans[client_id].remove(film_id)
        self.write_all_loans()

    def set_loans(self, loans):
        self.__loans = loans

    def read_all_loans(self):
        with open(self.__db_loans, "r") as f:
            lines = f.readlines()
            loans = {}
            for line in lines:
                parts = line.split(",")
                client_id = int(parts[0])
                films_ids = []
                for i in range(1, len(parts)):
                    films_ids.append(int(parts[i]))
                loans[client_id] = films_ids
            self.set_loans(loans)

    def write_all_loans(self):
        with open(self.__db_loans, "w") as f:
            loans = self.__loans
            for key in loans:
                client_id = key
                films_ids = loans[key]
                line = f"{client_id}"
                for id in films_ids:
                    line += f",{id}"
                line += "\n"
                f.write(line)