from lab7_9.errors.RepoError import RepoError
from lab7_9.model.Client import Client


class ClientsRepo:
    """
    Repozitoriu pentru gestionarea obiectelor Client.

    Functionalități principale:
    - stochează clienți într-o listă internă privată
    - adaugă clienți noi, verificând unicitatea ID-ului și CNP-ului
    - șterge clienți existenți
    - actualizează un client existent
    - caută un client după ID
    """

    def __init__(self):
        """
        Inițializează un repo gol de clienți.
        """
        self.__clients = []
        self.__db_clients = "/Users/eduardmocanu/School/fundamentele programarii sem 1 an 1/lab7_9/db/clients.txt"

    def get_all_clients(self):
        """
        Returnează o listă cu toți clienții existenți.
        """
        self.read_all_clients()
        return list(self.__clients)

    def add_client(self, client: Client):
        """
        Adaugă un client nou.

        Verifică:
        - dacă ID-ul clientului există deja -> RepoError
        - dacă CNP-ul clientului există deja -> RepoError
        """
        self.read_all_clients()
        if self.find_by_id(client.get_id()) is not None:
            raise RepoError("Clientul cu acest ID deja exista")
        for i in self.__clients:
            if i.get_CNP() == client.get_CNP():
                raise RepoError("Clientul cu acest CNP deja exista")
        self.__clients.append(client)
        self.write_all_clients()

    def remove(self, client: Client):
        """
        Șterge un client existent.

        Aruncă RepoError dacă clientul nu există.
        """
        self.read_all_clients()
        if self.find_by_id(client.get_id()) is None:
            raise RepoError("Acest client nu exista")
        self.__clients.remove(client)
        self.write_all_clients()

    def update(self, client_old_id, client_new: Client):
        """
        Actualizează un client existent cu datele unui alt client.

        Parametri:
        - client_old_id: ID-ul clientului existent
        - client_new: obiect Client cu noile valori
        """
        self.read_all_clients()
        for i in self.__clients:
            if i.get_id() == client_old_id:
                i.set_id(client_new.get_id())
                i.set_nume(client_new.get_nume())
                i.set_CNP(client_new.get_CNP())
                break
        self.write_all_clients()

    def find_by_id(self, client_id: int):
        """
        Caută un client după ID.

        Returnează:
        - obiect Client dacă este găsit
        - None dacă nu există
        """
        self.read_all_clients()
        for client in self.__clients:
            if client.get_id() == client_id:
                return client
        return None

    def set_clients(self, clients):
        self.__clients = clients

    def read_all_clients(self):
        with open(self.__db_clients, "r") as f:
            lines = f.readlines()
            clients = []
            for line in lines:
                if line == "":
                    break
                parts = line.split(",")
                client_id = int(parts[0])
                client_name = parts[1].strip()
                client_CNP = parts[2].strip()
                client = Client(client_id, client_name, client_CNP)
                clients.append(client)
            self.set_clients(clients)

    def write_all_clients(self):
        with open(self.__db_clients, "w") as f:
            for client in self.__clients:
                client_id = client.get_id()
                client_name = client.get_nume()
                client_CNP = client.get_CNP()
                f.write(f"{client_id},{client_name},{client_CNP}\n")
