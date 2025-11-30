import unittest

from lab7_9.errors.ServiceError import ServiceError
from lab7_9.model.Client import Client
from lab7_9.validators.client_validator import Client_validator


class TestClientValidator(unittest.TestCase):

    def setUp(self):
        self.validator = Client_validator()

    def test_verify_client(self):
        client = Client(1, "Test", "1111111111111")
        self.assertIsNone(self.validator.verify_client(client))

        with self.assertRaises(ServiceError):
            self.validator.verify_client(Client(1, "", "1234412411111"))

        with self.assertRaises(ServiceError):
            self.validator.verify_client(Client(1, "Edy", "1234"))

        with self.assertRaises(ServiceError):
            self.validator.verify_client(Client(-11, "Edy", "1234412411111"))

    def test_id_verification(self):
        self.assertIsNone(self.validator.id_verification(1))

        with self.assertRaises(ServiceError):
            self.validator.id_verification(-1)

