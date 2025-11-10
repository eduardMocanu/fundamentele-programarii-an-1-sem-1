from lab7_9.repository.clients_repo import ClientsRepo
from lab7_9.model.Client import Client


class Clients_service:
    def __init__(self, clients_repo: ClientsRepo, validator_client):
        self.__clients_repo = clients_repo
        self.__validator_client = validator_client

    def add_client(self, client_id, client_name, client_CNP):
        client = Client(client_id, client_name, client_CNP)
        self.__validator_client.verify_client(client)
        self.__clients_repo.add(client)

    def remove_client_by_id(self, client_id: int):
        self.__validator_client.id_verification(client_id)
        client = self.__clients_repo.find_by_id(client_id)
        self.__validator_client.verify_client(client)
        self.__clients_repo.remove(client)

    def modify_client(self, client_id_old: int, client_new_id, client_new_name, client_new_cnp):
        client_new = Client(client_new_id, client_new_name, client_new_cnp)
        self.__validator_client.verify_client(client_new)
        client_old = self.__clients_repo.find_by_id(client_id_old)
        self.__validator_client.verify_client(client_old)
        self.__clients_repo.update(client_old, client_new)

    def search_client_by_id(self, client_id: int):
        self.__validator_client.id_verification(client_id)
        client = self.__clients_repo.find_by_id(client_id)
        self.__validator_client.verify_client(client)
        return client

    def get_clients(self):
        return self.__clients_repo.get_all()