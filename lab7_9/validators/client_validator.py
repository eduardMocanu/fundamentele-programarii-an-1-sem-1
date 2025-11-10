from lab7_9.errors.ServiceError import ServiceError


class Client_validator:

    def verify_client(self, client):
        if client == None:
            raise ServiceError("client invalid")
        if client.get_id() <= 0:
            raise ServiceError("id invalid")
        if len(client.get_nume()) == 0:
            raise ServiceError("nume invalid")
        if len(client.get_CNP()) != 13:
            raise ServiceError("CNP invalid")

    def id_verification(self, client_id):
        if client_id <= 0:
            raise ServiceError("id invalid")

