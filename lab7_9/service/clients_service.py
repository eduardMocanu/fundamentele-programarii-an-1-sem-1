from lab7_9.repository.clients_repo import ClientsRepo
from lab7_9.model.Client import Client


class Clients_service:
    """
    Serviciu pentru gestionarea operațiunilor asupra clienților.

    Funcționalități principale:
    - adaugă clienți noi după validarea lor
    - șterge clienți existenți după ID
    - modifică datele unui client existent
    - caută un client după ID
    - returnează lista tuturor clienților
    """

    def __init__(self, clients_repo: ClientsRepo, validator_client):
        """
        Inițializează serviciul cu un repo de clienți și un validator de clienți.
        """
        self.__clients_repo = clients_repo
        self.__validator_client = validator_client

    def add_client(self, client_id, client_name, client_CNP):
        """
        Creează și adaugă un client după validarea datelor sale.

        Parametri:
        - client_id: ID-ul clientului
        - client_name: numele clientului
        - client_CNP: CNP-ul clientului
        """
        client = Client(client_id, client_name, client_CNP)
        self.__validator_client.verify_client(client)
        self.__clients_repo.add(client)

    def remove_client_by_id(self, client_id: int):
        """
        Șterge un client existent după ID, după ce verifică validitatea ID-ului și existența clientului.

        Parametri:
        - client_id: ID-ul clientului de șters
        """
        self.__validator_client.id_verification(client_id)
        client = self.__clients_repo.find_by_id(client_id)
        self.__validator_client.verify_client(client)
        self.__clients_repo.remove(client)

    def modify_client(self, client_id_old: int, client_new_id, client_new_name, client_new_cnp):
        """
        Modifică datele unui client existent cu noile valori furnizate.

        Parametri:
        - client_id_old: ID-ul clientului existent
        - client_new_id: noul ID
        - client_new_name: noul nume
        - client_new_cnp: noul CNP
        """
        client_new = Client(client_new_id, client_new_name, client_new_cnp)
        self.__validator_client.verify_client(client_new)
        client_old = self.__clients_repo.find_by_id(client_id_old)
        self.__validator_client.verify_client(client_old)
        self.__clients_repo.update(client_old, client_new)

    def search_client_by_id(self, client_id: int):
        """
        Caută și returnează un client după ID, după validarea ID-ului și existenței clientului.

        Parametri:
        - client_id: ID-ul clientului căutat

        Returnează:
        - obiect Client dacă este găsit
        """
        self.__validator_client.id_verification(client_id)
        client = self.__clients_repo.find_by_id(client_id)
        self.__validator_client.verify_client(client)
        return client

    def get_clients(self):
        """
        Returnează lista tuturor clienților existenți.
        """
        return self.__clients_repo.get_all()