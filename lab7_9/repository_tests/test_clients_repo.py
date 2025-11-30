import unittest
from lab7_9.model.Client import Client
from lab7_9.repository.in_memory.clients_repo import ClientsRepo


class TestClientsRepo(unittest.TestCase):

    def test_add_client(self):
        repo = ClientsRepo()
        test_client = Client(1, "Edy", "1234567891234")
        repo.add_client(test_client)
        self.assertIn(test_client, repo.get_all_clients())

    def test_remove_client(self):
        repo = ClientsRepo()
        test_client = Client(1, "Edy", "1234567891234")
        repo.add_client(test_client)
        repo.remove(test_client)
        self.assertNotIn(test_client, repo.get_all_clients())

    def test_modify_client(self):
        repo = ClientsRepo()
        original = Client(1, "Edy", "1234567891234")
        repo.add_client(original)
        updated = Client(2, "test", "0000000000000")

        repo.update(original.get_id(), updated)
        clients = repo.get_all_clients()

        self.assertTrue(
            any(client.get_id() == 2 and
                client.get_CNP() == "0000000000000" and
                client.get_nume() == "test"
                for client in clients)
        )

    def test_get_clients(self):
        repo = ClientsRepo()
        c1 = Client(1, "Edy", "1234567891234")
        c2 = Client(2, "test", "0000000000000")

        repo.add_client(c1)
        repo.add_client(c2)

        self.assertIn(c1, repo.get_all_clients())
        self.assertIn(c2, repo.get_all_clients())
