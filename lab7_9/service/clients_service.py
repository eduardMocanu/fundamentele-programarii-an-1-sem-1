from lab7_9.repository.clients_repo import ClientsRepo
from lab7_9.model.Client import Client


class Clients_service:
    def __init__(self, clients_repo: ClientsRepo):
        self.__clients_repo = clients_repo

    def add_client(self, client: Client):
        existing = self.__clients_repo.find_by_id(client.get_id())
        if existing is not None:
            raise ValueError("Clientul cu acest ID exista deja.")
        self.__clients_repo.add(client)

    def remove_client(self, client_id: int):
        client = self.__clients_repo.find_by_id(client_id)
        if client is None:
            raise ValueError("Nu exista un client cu acest ID.")
        self.__clients_repo.remove(client)

    def modify_client(self, client_id_old: int, client_new: Client):
        client_old = self.__clients_repo.find_by_id(client_id_old)
        if client_old is None:
            raise ValueError("Nu exista un client cu acest ID.")
        self.__clients_repo.update(client_old, client_new)

    def search_client_by_id(self, client_id: int):
        client = self.__clients_repo.find_by_id(client_id)
        if client is None:
            raise ValueError("Nu exista un client cu acest ID.")
        return client

    def get_clients(self):
        return self.__clients_repo.get_all()