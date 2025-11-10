from ..service.clients_service import Clients_service
from ..errors.ServiceError import ServiceError
from ..repository.clients_repo import ClientsRepo
from ..validators.client_validator import Client_validator


def test_add_client():
    clients_repo = ClientsRepo()
    clients_validators = Client_validator()
    clients_service = Clients_service(clients_repo, clients_validators)

    try:
        clients_service.add_client(1, "Edy", "1234")
        assert False, "ServiceError should have been raised"
    except ServiceError:
        assert True

    clients_service.add_client(1, "Test", "1234567890123")

    stored_clients = clients_service.get_clients()
    assert any(
        c.id == 1 and c.name == "Test" and c.cnp == "1234567890123"
        for c in stored_clients
    ), "Client should be in the repository"


def test_remove_client_by_id():
    clients_repo = ClientsRepo()
    clients_validators = Client_validator()
    clients_service = Clients_service(clients_repo, clients_validators)

    clients_service.add_client(1, "Test", "1234567890123")

    clients_service.remove_client_by_id(1)
    stored_clients = clients_service.get_clients()
    assert all(c.id != 1 for c in stored_clients), "Client should be removed"

    try:
        clients_service.remove_client_by_id(999)
        assert False, "ServiceError should have been raised"
    except ServiceError:
        assert True


def test_modify_client():
    clients_repo = ClientsRepo()
    clients_validators = Client_validator()
    clients_service = Clients_service(clients_repo, clients_validators)

    clients_service.add_client(1, "Test", "1234567890123")

    clients_service.modify_client(1, 1, "Modified", "9876543210987")

    stored_clients = clients_service.get_clients()
    modified = next((c for c in stored_clients if c.id == 1), None)
    assert modified is not None, "Client should exist"
    assert modified.name == "Modified"
    assert modified.cnp == "9876543210987"

    try:
        clients_service.modify_client(8, 999, "NoOne", "0000000000000")
        assert False, "ServiceError should have been raised"
    except ServiceError:
        assert True


def test_search_client_by_id():
    clients_repo = ClientsRepo()
    clients_validators = Client_validator()
    clients_service = Clients_service(clients_repo, clients_validators)

    clients_service.add_client(1, "Test", "1234567890123")

    found_client = clients_service.search_client_by_id(1)
    assert found_client.id == 1
    assert found_client.name == "Test"
    assert found_client.cnp == "1234567890123"

    try:
        clients_service.search_client_by_id(999)
        assert False, "ServiceError should have been raised"
    except ServiceError:
        assert True


def test_get_clients():
    clients_repo = ClientsRepo()
    clients_validators = Client_validator()
    clients_service = Clients_service(clients_repo, clients_validators)

    assert clients_service.get_clients() == []

    clients_service.add_client(1, "Alice", "1234567890123")
    clients_service.add_client(2, "Bob", "9876543210987")

    stored_clients = clients_service.get_clients()
    assert any(c.id == 1 and c.name == "Alice" for c in stored_clients)
    assert any(c.id == 2 and c.name == "Bob" for c in stored_clients)
    assert len(stored_clients) == 2

def tests_service_clients():
    test_add_client()
    test_modify_client()
    test_remove_client_by_id()
    test_get_clients()
    test_search_client_by_id()