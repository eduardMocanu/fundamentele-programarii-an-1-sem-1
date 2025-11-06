from lab7_9.model.Client import Client


class Clients_repo:

    def __init__(self):
        self.__clients = []

    def get_clients(self):
        return self.__clients

    def add_client(self, client):
        for i in self.__clients:
            if i.get_id() == client.get_id():
                return "exista un client cu acest ID"
        self.__clients.append(client)
        return ""

    def remove_client(self, client_id):
        for i in self.__clients:
            if i.get_id() == client_id:
                self.__clients.remove(i)
                return ""
        return "nu exista un client cu acest ID"

    def modify_client(self, client_id_old, client_new:Client):
        for i in self.__clients:
            if i.get_id == client_id_old:
                i.set_id(client_new.get_id())
                i.set_nume(client_new.get_nume())
                i.set_CNP(client_new.get_CNP())
                return ""
        return "nu exista un client cu acest ID"

    def search_client_by_id(self, client_id):
        for i in self.__clients:
            if i.get_id() == client_id:
                return i
        return None