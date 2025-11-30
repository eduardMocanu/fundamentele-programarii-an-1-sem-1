import unittest
import random

from lab7_9.service.clients_service import Clients_service
from lab7_9.errors.ServiceError import ServiceError
from lab7_9.repository.in_memory.clients_repo import ClientsRepo
from lab7_9.validators.client_validator import Client_validator


class TestClientsService(unittest.TestCase):

    def setUp(self):
        self.repo = ClientsRepo()
        self.validator = Client_validator()
        self.service = Clients_service(self.repo, self.validator)

    def test_add_client(self):
        with self.assertRaises(ServiceError):
            self.service.add_client(1, "Edy", "1234")

        self.service.add_client(1, "Test", "1234567890123")
        stored = self.service.get_clients()

        self.assertTrue(
            any(
                c.get_id() == 1 and
                c.get_nume() == "Test" and
                c.get_CNP() == "1234567890123"
                for c in stored
            )
        )

    def test_remove_client_by_id(self):
        self.service.add_client(1, "Test", "1234567890123")
        self.service.remove_client_by_id(1)

        stored = self.service.get_clients()
        self.assertTrue(all(c.get_id() != 1 for c in stored))

        with self.assertRaises(ServiceError):
            self.service.remove_client_by_id(999)

    def test_modify_client(self):
        self.service.add_client(1, "Test", "1234567890123")

        self.service.modify_client(1, 1, "Modified", "9876543210987")

        stored = self.service.get_clients()
        modified = next((c for c in stored if c.get_id() == 1), None)

        self.assertIsNotNone(modified)
        self.assertEqual(modified.get_nume(), "Modified")
        self.assertEqual(modified.get_CNP(), "9876543210987")

        with self.assertRaises(ServiceError):
            self.service.modify_client(8, 999, "NoOne", "0000000000000")

    def test_search_client_by_id(self):
        self.service.add_client(1, "Test", "1234567890123")

        found = self.service.search_client_by_id(1)
        self.assertEqual(found.get_id(), 1)
        self.assertEqual(found.get_nume(), "Test")
        self.assertEqual(found.get_CNP(), "1234567890123")

        with self.assertRaises(ServiceError):
            self.service.search_client_by_id(999)

    def test_get_clients(self):
        self.assertEqual(self.service.get_clients(), [])

        self.service.add_client(1, "Alice", "1234567890123")
        self.service.add_client(2, "Bob", "9876543210987")

        stored = self.service.get_clients()

        self.assertTrue(any(c.get_id() == 1 and c.get_nume() == "Alice" for c in stored))
        self.assertTrue(any(c.get_id() == 2 and c.get_nume() == "Bob" for c in stored))
        self.assertEqual(len(stored), 2)

    def test_random_clients(self):
        random.seed(99)
        self.service.random_clients()

        random.seed(99)
        _ = random.randint(1, 10)

        self.assertTrue(
            any(client.get_id() == 49907 for client in self.repo.get_all_clients())
        )

        length = random.randint(1, 15)
        self.assertEqual(length, 7)

