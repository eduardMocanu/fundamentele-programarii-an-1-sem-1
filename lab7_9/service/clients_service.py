from lab7_9.repository.clients_repo import Clients_repo


class Clients_service:

    def __init__(self, clients_repo:Clients_repo):
        self.__clients_repo = clients_repo

    def add_client(self, client):
        return self.__clients_repo.add_client(client)

    def remove_client(self, client_id):
        return self.__clients_repo.remove_client(client_id)

    def modify_client(self, client_id_old, client):
        return self.__clients_repo.modify_client(client_id_old, client)

    def search_client_by_id(self, client_id):
        return self.__clients_repo.search_client_by_id(client_id)

    def get_clients(self):
        return self.__clients_repo.get_clients()