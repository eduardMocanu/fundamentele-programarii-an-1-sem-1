from lab7_9.model.Client import Client
from lab7_9.repository.clients_repo import ClientsRepo


def test_add_client():
    repo = ClientsRepo()
    test_client = Client(1, "Edy", "1234567891234")
    repo.add_client(test_client)
    assert test_client in repo.get_all_clients()

def test_remove_client():
    repo = ClientsRepo()
    test_client = Client(1, "Edy", "1234567891234")
    repo.add_client(test_client)
    repo.remove(test_client)
    assert test_client not in repo.get_all_clients()

def test_modify_client():
    repo = ClientsRepo()
    test_client = Client(1, "Edy", "1234567891234")
    repo.add_client(test_client)
    test_client_update = Client(2, "test", "0000000000000")
    repo.update(test_client.get_id(), test_client_update)
    clients= repo.get_all_clients()
    assert any(client.get_id() == 2 and client.get_CNP() == "0000000000000" and client.get_nume() == "test" for client in clients)

def test_get_clients():
    repo = ClientsRepo()
    test_client = Client(1, "Edy", "1234567891234")
    repo.add_client(test_client)
    test_client1 = Client(2, "test", "0000000000000")
    repo.add_client(test_client1)
    assert test_client in repo.get_all_clients()
    assert test_client1 in repo.get_all_clients()

def test_clients_repo():
    test_add_client()
    test_get_clients()
    test_modify_client()
    test_remove_client()