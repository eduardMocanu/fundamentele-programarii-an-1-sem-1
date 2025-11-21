from lab7_9.errors.RepoError import RepoError
from lab7_9.errors.ServiceError import ServiceError
from lab7_9.errors.UIerror import UiError


class UI:
    """
    Interfață pentru utilizator (UI) care gestionează comenzile pentru clienți, filme și împrumuturi.

    Funcționalități principale:
    - rulează bucla principală de input pentru utilizator
    - permite adăugarea, ștergerea și modificarea clienților
    - afișează meniul de ajutor cu comenzile disponibile
    - gestionează erorile și le afișează utilizatorului
    """

    def __init__(self, client_service, film_service, loan_service):
        """
        Inițializează UI-ul cu serviciile corespunzătoare.

        Parametri:
        - client_service: serviciul pentru operațiuni cu clienți
        - film_service: serviciul pentru operațiuni cu filme
        - lending_service: serviciul pentru operațiuni cu împrumuturi
        """
        self.__client_service = client_service
        self.__film_service = film_service
        self.__loan_service = loan_service
        self.__comenzi = {
            "help": self.help_menu,
            "add_client": self.add_client,
            "remove_client": self.remove_client,
            "modify_client": self.modify_client,
            "add_film": self.add_film,
            "remove_film": self.remove_film,
            "modify_film": self.modify_film,
            "random_clients":self.random_clients,
            "get_clients": self.get_all_clients,
            "get_films": self.get_all_films,
            "search_client_by_id": self.search_client_by_id,
            "search_film_by_id": self.search_film_by_id,
            "add_loan": self.add_loan,
            "remove_loan": self.remove_loan,
            "clients_loaned_films_sorted": self.clients_loaned_films_sorted,
            "most_loaned_films": self.most_loaned_films,
            "top_30_clients": self.top_30_clients

        }

    def help_menu(self):
        """
        Afișează lista comenzilor disponibile pentru utilizator.
        """
        print("Adauga client: add_client")
        print("Sterge client: remove_client")
        print("Modifica client: modify_client")
        print("Adauga film: add_film")
        print("Sterge film: remove_film")
        print("Modifica film: modify_film")
        print("Adauga clienti random: random_clients")
        print("Vezi clientii: get_clients")
        print("Vezi filmele: get_films")
        print("Cauta client dupa ID: search_client_by_id")
        print("Cauta film dupa ID: search_film_by_id")
        print("Adauga un imprumut: add_loan")
        print("Sterge un imprumut: remove_loan")
        print("Clienti sortati dupa numarul de filme inchiriate: clients_loaned_films_sorted")
        print("Cele mai inchiriate filme: most_loaned_films")
        print("Top 30% al clientilor dupa numarul de filme inchiriate: top_30_clients")

    def run(self):
        """
        Rulează bucla principală de input, așteptând comenzi de la utilizator.

        Comenzile suportate sunt:
        - add_client
        - remove_client
        - modify_client
        - help
        - exit
        """
        print("Introdu help pentru a vedea toate comenzile")
        while True:
            whole_command = input("Introdu comanda: ").lower().strip()
            splitted_command = whole_command.split(" ")
            if len(splitted_command) > 1:
                print("Comanda invalida, introdu help pentru a vedea toate comenzile")
                continue
            command = splitted_command[0]
            if command in self.__comenzi:
                self.__comenzi[command]()
            elif command == "exit":
                break
            else:
                print("Comanda invalida, introdu help pentru a vedea toate comenzile")
            print()
        print("bye")

    def add_client(self):
        """
        Solicită datele unui client de la utilizator și îl adaugă folosind serviciul de clienți.

        Gestionează erorile și le afișează utilizatorului:
        - ValueError pentru ID invalid
        - UiError, ServiceError, RepoError pentru probleme de validare sau repo
        """
        try:
            id_client = int(input("Introdu id-ul clientului: "))
        except ValueError:
            print("id invalid")
            return
        nume_client = input("Introdu numele clientului: ").strip().lower()
        CNP_client = input("Introdu CNP-ul clientului: ").strip()
        try:
            self.__client_service.add_client(id_client, nume_client, CNP_client)
        except UiError as e:
            print(e)
        except ServiceError as e:
            print(e)
        except RepoError as e:
            print(e)

    def remove_client(self):
        """
        Solicită ID-ul unui client de la utilizator și îl șterge folosind serviciul de clienți.

        Gestionează erorile și le afișează utilizatorului:
        - ValueError pentru ID invalid
        - UiError, ServiceError, RepoError pentru probleme de validare sau repo
        """
        try:
            id_client = int(input("Introdu id-ul clientului care doresti sa fie sters: "))
        except ValueError:
            print("id invalid")
            return
        try:
            self.__client_service.remove_client_by_id(id_client)
        except UiError as e:
            print(e)
        except ServiceError as e:
            print(e)
        except RepoError as e:
            print(e)

    def modify_client(self):
        """
        Solicită ID-ul vechi și noile date ale clientului și modifică înregistrarea existentă.

        Gestionează erorile și le afișează utilizatorului:
        - ValueError pentru ID invalid
        - UiError, ServiceError, RepoError pentru probleme de validare sau repo
        """
        try:
            id_client_old = int(input("Introdu id-ul vechii inregistrari: "))
        except ValueError:
            print("Id vechi invalid")
            return
        try:
            id_client_new = int(input("Introdu noul id al clientului: "))
        except ValueError:
            print("Id nou invalid")
            return
        nume_client_new = input("Introdu noul nume al clientului: ").strip().lower()
        CNP_client_new = input("Introdu noul CNP al clientului: ").strip()
        try:
            self.__client_service.modify_client(id_client_old, id_client_new, nume_client_new, CNP_client_new)
        except UiError as e:
            print(e)
        except ServiceError as e:
            print(e)
        except RepoError as e:
            print(e)


    def add_film(self):
        """
        Solicită datele unui film de la utilizator și îl adaugă folosind serviciul de filme.

        Gestionează erorile și le afișează utilizatorului:
        - ValueError pentru ID invalid
        - UiError, ServiceError, RepoError pentru probleme de validare sau repo
        """
        try:
            id_film = int(input("Introdu id-ul filmului: "))
        except ValueError:
            print("Id invalid")
            return
        titlu_film = input("Introdu titlul filmului: ").strip().lower()
        descriere_film = input("Introdu descrierea filmului: ").strip().lower()
        gen_film = input("Introdu genul filmului: ").strip().lower()
        try:
            self.__film_service.add_film(id_film, titlu_film, descriere_film, gen_film)
        except UiError as e:
            print(e)
        except ServiceError as e:
            print(e)
        except RepoError as e:
            print(e)

    def remove_film(self):
        """
        Solicită ID-ul unui film de la utilizator și îl șterge folosind serviciul de filme.

        Gestionează erorile și le afișează utilizatorului:
        - ValueError pentru ID invalid
        - UiError, ServiceError, RepoError pentru probleme de validare sau repo
        """
        try:
            id_film = int(input("Introdu id-ul filmului care doresti sa fie sters: "))
        except ValueError:
            print("id invalid")
            return
        try:
            self.__film_service.remove_film_by_id(id_film)
        except UiError as e:
            print(e)
        except ServiceError as e:
            print(e)
        except RepoError as e:
            print(e)

    def modify_film(self):
        """
        Solicită ID-ul vechi și noile date ale filmului și modifică înregistrarea existentă.

        Gestionează erorile și le afișează utilizatorului:
        - ValueError pentru ID invalid
        - UiError, ServiceError, RepoError pentru probleme de validare sau repo
        """
        try:
            id_film_old = int(input("Introdu id-ul vechii inregistrari: "))
        except ValueError:
            print("Id vechi invalid")
            return
        try:
            id_film_new = int(input("Introdu noul id al filmului: "))
        except ValueError:
            print("Id nou invalid")
            return
        titlu_film_new = input("Introdu titlul filmului").strip().lower()
        descriere_film_new = input("Introdu descrierea filmului").strip().lower()
        gen_film_new = input("Introdu genul filmului").strip().lower()
        try:
            self.__film_service.modify_film(id_film_old, id_film_new, titlu_film_new, descriere_film_new, gen_film_new)
        except UiError as e:
            print(e)
        except ServiceError as e:
            print(e)
        except RepoError as e:
            print(e)

    def search_film_by_id(self):
        """
        Caută un film după ID citit de la tastatură.

        - Cere utilizatorului un ID numeric.
        - Validează inputul (handle ValueError).
        - Apelează serviciul film_service pentru a căuta filmul.
        - Tratează erorile specifice (UiError, ServiceError, RepoError).
        - Dacă filmul este găsit, îl afișează.
        """
        try:
            id_film = int(input("Introdu id-ul filmului pe care vrei sa il cauti: "))
        except ValueError:
            print("id invalid")
            return

        try:
            film = self.__film_service.search_film_by_id(id_film)
        except UiError as e:
            print(e)
            return
        except ServiceError as e:
            print(e)
            return
        except RepoError as e:
            print(e)
            return
        print(film)

    def random_clients(self):
        """
        Generează o listă de clienți aleatorii prin intermediul client_service.
        """
        self.__client_service.random_clients()

    def get_all_clients(self):
        """
        Afișează toți clienții existenți în sistem.
        """
        print(self.__client_service.get_clients())

    def get_all_films(self):
        """
        Afișează toate filmele existente în sistem.
        """
        print(self.__film_service.get_films())

    def add_loan(self):
        """
        Creează un nou împrumut între un client și un film.

        - Solicită ID-ul clientului și ID-ul filmului.
        - Validează inputul numeric.
        - Apelează loan_service pentru a înregistra împrumutul.
        - Tratează erorile din UI, servicii sau repo.
        """
        try:
            id_client = int(input("Introdu id-ul clientului pe care vrei sa il asociezi imprumutului: "))
        except ValueError:
            print("id invalid")
            return
        try:
            id_film = int(input("Introdu id-ul filmului pe care vrei sa il asociezi imprumutului: "))
        except ValueError:
            print("id invalid")
            return
        try:
            self.__loan_service.add_loan(id_client, id_film)
        except UiError as e:
            print(e)
            return
        except ServiceError as e:
            print(e)
            return
        except RepoError as e:
            print(e)
            return

    def remove_loan(self):
        """
        Elimină (închide) un împrumut existent între un client și un film.

        - Solicită ID-ul clientului și ID-ul filmului.
        - Validează inputul numeric.
        - Apelează loan_service pentru a elimina împrumutul.
        - Tratează erorile din UI, servicii sau repo.
        """
        try:
            id_client = int(input("Introdu id-ul clientului al carui imprumut este finalizat: "))
        except ValueError:
            print("id invalid")
            return
        try:
            id_film = int(input("Introdu id-ul filmului pe care il doresti restituit: "))
        except ValueError:
            print("id invalid")
            return
        try:
            self.__loan_service.remove_loan(id_client, id_film)
        except UiError as e:
            print(e)
            return
        except ServiceError as e:
            print(e)
            return
        except RepoError as e:
            print(e)
            return

    def clients_loaned_films_sorted(self):
        """
        Afișează clienții și numărul lor de împrumuturi,
        ordonați după numărul de împrumuturi (crescator).

        - Apelează loan_service pentru a obține lista sortată.
        - Tratează erorile posibile.
        - Afișează fiecare pereche (nume, număr împrumuturi).
        """
        try:
            result = self.__loan_service.clients_loaned_films_sorted()
        except UiError as e:
            print(e)
            return
        except ServiceError as e:
            print(e)
            return
        except RepoError as e:
            print(e)
            return
        for i in result:
            print(f"Nume: {i[0]}, Numar inchirieri: {i[1]}")

    def most_loaned_films(self):
        """
        Afișează filmele ordonate după numărul de împrumuturi (descrescător).

        - Apelează loan_service pentru a obține statistica.
        - Tratează erorile specifice.
        - Afișează lista rezultată.
        """
        try:
            result = self.__loan_service.most_loaned_films()
        except UiError as e:
            print(e)
            return
        except ServiceError as e:
            print(e)
            return
        except RepoError as e:
            print(e)
            return
        for i in result:
            print(i)

    def top_30_clients(self):
        """
        Afișează primii 30% de clienți cu cele mai multe împrumuturi.

        - Apelează loan_service pentru a calcula topul.
        - Tratează erorile specifice.
        - Afișează fiecare client cu numărul său de împrumuturi.
        """
        try:
            result = self.__loan_service.top_30_clients()
        except UiError as e:
            print(e)
            return
        except ServiceError as e:
            print(e)
            return
        except RepoError as e:
            print(e)
            return
        for i in result:
            print(f"Nume: {i[0]}, Numar inchirieri: {i[1]}")

    def search_client_by_id(self):
        """
        Caută un client după ID citit de la tastatură.

        - Cere utilizatorului să introducă un ID numeric.
        - Validează inputul.
        - Apelează client_service pentru căutare.
        - Tratează erorile din UI, servicii și repo.
        - Dacă clientul există, îl afișează.
        """
        try:
            id_client = int(input("Introdu id-ul clientului pe care doresti sa il cauti: "))
        except ValueError:
            print("id invalid")
            return
        try:
            client = self.__client_service.search_client_by_id(id_client)
        except UiError as e:
            print(e)
            return
        except ServiceError as e:
            print(e)
            return
        except RepoError as e:
            print(e)
            return

        print(client)