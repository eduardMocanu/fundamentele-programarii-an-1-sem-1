from lab7_9.Validators import Validators
from lab7_9.model.Client import Client
from lab7_9.service.clients_service import q


class Clients_controller:

    def __init__(self, clients_service:Clients_service, validator:Validators):
        self.__clients_service = clients_service
        self.__validator = validator

    def add_client(self, client_id, client_name, client_CNP):
        if not self.__validator.check_int(client_id):
            return "Valoarea id-ului este invalida"
        if not self.__validator.check_int(client_CNP):
            return "valoarea cnp-ului este invalida"
        try:
            self.__clients_service.add_client(Client(int(client_id), client_name, int(client_CNP)))
        except ValueError as e:
            return str(e)

    def remove_client(self, client_id):
        if not self.__validator.check_int(client_id):
            return "valoarea id-ului este invalida"
        try:
            self.__clients_service.remove_client(int(client_id))
        except ValueError as e:
            return str(e)

    def modify_client(self, client_id_old, client_id_new, client_name_new, client_CNP_new):
        if not self.__validator.check_int(client_id_old):
            return "id-ul vechi al clientului este invalid"
        if not self.__validator.check_int(client_id_new):
            return "id-ul nou al clientului este invalid"
        if not self.__validator.check_int(client_CNP_new):
            return "cnp-ul nou al clientului este invalid"
        try:
            self.__clients_service.modify_client(client_id_old, Client(client_id_new, client_name_new, client_CNP_new))
        except ValueError as e:
            return str(e)