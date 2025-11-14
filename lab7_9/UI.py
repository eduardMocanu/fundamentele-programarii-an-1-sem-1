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

    def __init__(self, client_service, film_service, lending_service):
        """
        Inițializează UI-ul cu serviciile corespunzătoare.

        Parametri:
        - client_service: serviciul pentru operațiuni cu clienți
        - film_service: serviciul pentru operațiuni cu filme
        - lending_service: serviciul pentru operațiuni cu împrumuturi
        """
        self.__client_service = client_service
        self.__film_service = film_service
        self.__lending_service = lending_service
        self.__comenzi = {
            "help": self.help_menu,
            "add_client": self.add_client,
            "remove_client": self.remove_client,
            "modify_client": self.modify_client,
            "add_film": self.add_film,
            "remove_film": self.remove_film,
            "modify_film": self.modify_film
        }

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
        nume_client = input("Introdu numele clientului: ").strip()
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
        nume_client_new = input("Introdu noul nume al clientului: ").strip()
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
        titlu_film = input("Introdu titlul filmului").strip()
        descriere_film = input("Introdu descrierea filmului").strip()
        gen_film = input("Introdu genul filmului").strip()
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
        titlu_film_new = input("Introdu titlul filmului")
        descriere_film_new = input("Introdu descrierea filmului").strip()
        gen_film_new = input("Introdu genul filmului").strip()
        try:
            self.__film_service.modify_film(id_film_old, id_film_new, titlu_film_new, descriere_film_new, gen_film_new)
        except UiError as e:
            print(e)
        except ServiceError as e:
            print(e)
        except RepoError as e:
            print(e)


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

