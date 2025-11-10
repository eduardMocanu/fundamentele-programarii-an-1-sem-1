from lab7_9.model.Client import Client
from lab7_9.repository.clients_repo import ClientsRepo


def test_add_client():
    repo = ClientsRepo()
    test_client = Client(1, "Edy", "1234567891234")
    repo.add(test_client)
    assert test_client in repo.get_all()

def test_remove_client():
    repo = ClientsRepo()
    test_client = Client(1, "Edy", "1234567891234")
    repo.add(test_client)
    repo.remove(test_client)
    assert test_client not in repo.get_all()

def test_modify_client():
    repo = ClientsRepo()
    test_client = Client(1, "Edy", "1234567891234")
    repo.add(test_client)
    test_client_update = Client(2, "test", "0000000000000")
    repo.update(test_client.get_id(), test_client_update)
    assert test_client_update in repo.get_all()

def test_get_clients():
    repo = ClientsRepo()
    test_client = Client(1, "Edy", "1234567891234")
    repo.add(test_client)
    test_client1 = Client(2, "test", "0000000000000")
    repo.add(test_client1)
    assert test_client in repo.get_all()
    assert test_client1 in repo.get_all()

def test_clients_repo():
    test_add_client()
    test_get_clients()
    test_modify_client()
    test_remove_client()