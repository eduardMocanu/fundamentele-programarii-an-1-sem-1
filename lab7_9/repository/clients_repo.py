from lab7_9.model.Client import Client


class ClientsRepo:
    def __init__(self):
        self.__clients = []

    def get_all(self):
        return list(self.__clients)

    def add(self, client: Client):
        self.__clients.append(client)

    def remove(self, client: Client):
        self.__clients.remove(client)

    def update(self, client_old_id, client_new: Client):
        for i in self.__clients:
            if i.get_id() == client_old_id:
                i.set_id(client_new.get_id())
                i.set_nume(client_new.get_nume())
                i.set_CNP(client_new.get_CNP())
                break

    def find_by_id(self, client_id: int):
        for client in self.__clients:
            if client.get_id() == client_id:
                return client
        return None