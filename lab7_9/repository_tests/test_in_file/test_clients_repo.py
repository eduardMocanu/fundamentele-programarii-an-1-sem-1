import unittest
from lab7_9.model.Client import Client
from lab7_9.repository.in_file.clients_repo import ClientsRepo


class TestClientsRepo(unittest.TestCase):

    file_db_clients = "/Users/eduardmocanu/School/fundamentele programarii sem 1 an 1/lab7_9/repository_tests/test_in_file/test_db/test_clients.txt"
    repo = ClientsRepo(file_db_clients)

    def setUp(self):
        self.helper_add_data()
        self.repo = ClientsRepo(self.file_db_clients)

    def tearDown(self):
        with open(self.file_db_clients, "w") as f:
            pass

    def helper_add_data(self):
        with open(self.file_db_clients, "w") as f:
            f.writelines(["1,T,2523682071544\n", "2,E,4812163181100\n", "3,S,9251009283280\n", "4,T,2423929019089\n"])

    def test_add_client(self):
        test_client = Client(7, "Edy", "1234567891234")
        self.repo.add_client(test_client)
        self.assertIn(test_client, self.repo.get_all_clients())

    def test_remove_client(self):
        test_client = Client(1, "T", "2523682071544")
        self.repo.remove(test_client)
        self.assertNotIn(test_client, self.repo.get_all_clients())

    def test_modify_client(self):
        self.repo.update(2, Client(3, "tttt", "0000000000000"))
        clients = self.repo.get_all_clients()

        self.assertTrue(
            any(client.get_id() == 3 and
                client.get_CNP() == "0000000000000" and
                client.get_nume() == "tttt"
                for client in clients)
        )

    def test_get_clients(self):
        c1 = Client(7, "Edy", "1234567891234")
        c2 = Client(8, "test", "0000000000000")

        self.repo.add_client(c1)
        self.repo.add_client(c2)

        self.assertIn(c1, self.repo.get_all_clients())
        self.assertIn(c2, self.repo.get_all_clients())
