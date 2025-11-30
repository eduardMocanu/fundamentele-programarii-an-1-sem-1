import unittest

from lab7_9.repository.in_memory.loans_repo import Loans_repo
from lab7_9.service.loans_service import Lending_service
from lab7_9.service.clients_service import Clients_service
from lab7_9.service.films_service import Films_service
from lab7_9.repository.in_memory.clients_repo import ClientsRepo
from lab7_9.repository.in_memory.films_repo import Films_repo
from lab7_9.validators.client_validator import Client_validator
from lab7_9.validators.film_validator import Film_validator
from lab7_9.errors.ServiceError import ServiceError
from lab7_9.errors.RepoError import RepoError


class TestLendingService(unittest.TestCase):

    def setUp(self):
        self.loans_repo = Loans_repo()
        self.clients_service = Clients_service(ClientsRepo(), Client_validator())
        self.films_service = Films_service(Films_repo(), Film_validator())
        self.service = Lending_service(
            self.loans_repo, self.clients_service, self.films_service
        )

    def test_add_loan(self):
        self.clients_service.add_client(1, "Edy", "1234567890123")
        self.films_service.add_film(10, "Film X", "Descriere", "test")

        self.service.add_loan(1, 10)
        self.assertEqual(self.loans_repo.get_loans(), {1: [10]})

        with self.assertRaises(RepoError):
            self.service.add_loan(1, 10)

        with self.assertRaises(ServiceError):
            self.service.add_loan(999, 10)

        with self.assertRaises(ServiceError):
            self.service.add_loan(1, 999)

    def test_remove_loan(self):
        self.clients_service.add_client(1, "Edy", "1234567890123")
        self.films_service.add_film(10, "Film X", "Descriere", "test")

        self.service.add_loan(1, 10)
        self.service.remove_loan(1, 10)
        self.assertEqual(self.loans_repo.get_loans(), {1: []})

        with self.assertRaises(RepoError):
            self.service.remove_loan(1, 10)

        with self.assertRaises(ServiceError):
            self.service.remove_loan(999, 10)

        with self.assertRaises(ServiceError):
            self.service.remove_loan(1, 999)

    def test_clients_loaned_films_sorted(self):
        self.clients_service.add_client(1, "Alex", "1234567890123")
        self.clients_service.add_client(2, "Edy", "1234567890129")
        self.films_service.add_film(10, "A", "desc", "test")
        self.films_service.add_film(20, "B", "desc", "test")

        self.service.add_loan(1, 10)
        self.service.add_loan(2, 10)
        self.service.add_loan(2, 20)

        result = self.service.clients_loaned_films_sorted()
        self.assertEqual(result, [["Alex", 1], ["Edy", 2]])

    def test_most_loaned_films(self):
        self.clients_service.add_client(1, "Edy", "1234567890123")
        self.clients_service.add_client(2, "Alex", "1234567890129")
        self.films_service.add_film(10, "Film X", "desc", "test")
        self.films_service.add_film(20, "Film Y", "desc", "test")

        self.service.add_loan(1, 10)
        self.service.add_loan(2, 10)
        self.service.add_loan(1, 20)

        result = self.service.most_loaned_films()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_titlu(), "Film X")

    def test_top_30_clients(self):
        self.clients_service.add_client(1, "Edy", "1111111111111")
        self.clients_service.add_client(2, "Alex", "2222222222222")
        self.clients_service.add_client(3, "Mihai", "3333333333333")
        self.films_service.add_film(10, "A", "desc", "test")
        self.films_service.add_film(20, "B", "desc", "test")

        self.service.add_loan(1, 10)
        self.service.add_loan(1, 20)
        self.service.add_loan(2, 10)

        result = self.service.top_30_clients()
        self.assertEqual(result, [["Edy", 2]])

