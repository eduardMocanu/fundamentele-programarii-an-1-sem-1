
from ..errors.ServiceError import ServiceError
from ..model.Client import Client
from ..validators.client_validator import Client_validator


def test_verify_client():
    client_validator = Client_validator()
    client = Client(1, "Test", "1111111111111")
    assert client_validator.verify_client(client) is None

    try:
        client_validator.verify_client(Client(1, "", "1234412411111"))
        assert False
    except ServiceError:
        assert True

    try:
        client_validator.verify_client(Client(1, "Edy", "1234"))
        assert False
    except ServiceError:
        assert True

    try:
        client_validator.verify_client(Client(-11, "Edy", "1234412411111"))
        assert False
    except ServiceError:
        assert True

def test_id_verification():
    client_validator = Client_validator()
    assert client_validator.id_verification(1) is None

    try:
        client_validator.id_verification(-1)
        assert False
    except ServiceError:
        assert True



def tests_client_validator():
    test_verify_client()
    test_id_verification()