import unittest
from lab7_9.repository.in_memory.loans_repo import Loans_repo
from lab7_9.errors.RepoError import RepoError


class TestLoansRepo(unittest.TestCase):

    def test_add_loan_new_client(self):
        repo = Loans_repo()
        repo.add_loan(1, 10)
        loans = repo.get_loans()

        self.assertIn(1, loans)
        self.assertEqual(loans[1], [10])

    def test_add_loan_existing_client_new_film(self):
        repo = Loans_repo()
        repo.add_loan(1, 10)
        repo.add_loan(1, 20)
        loans = repo.get_loans()

        self.assertEqual(loans[1], [10, 20])

    def test_add_loan_same_film_raises(self):
        repo = Loans_repo()
        repo.add_loan(1, 10)

        with self.assertRaises(RepoError):
            repo.add_loan(1, 10)

    def test_remove_loan_valid(self):
        repo = Loans_repo()
        repo.add_loan(1, 10)
        repo.add_loan(1, 20)

        repo.remove_loan(1, 10)
        loans = repo.get_loans()

        self.assertEqual(loans[1], [20])

    def test_remove_loan_nonexistent_client(self):
        repo = Loans_repo()

        with self.assertRaises(RepoError):
            repo.remove_loan(1, 10)

    def test_remove_loan_film_not_borrowed(self):
        repo = Loans_repo()
        repo.add_loan(1, 10)

        with self.assertRaises(RepoError):
            repo.remove_loan(1, 20)

    def test_get_loans_structure(self):
        repo = Loans_repo()
        repo.add_loan(1, 10)
        repo.add_loan(2, 50)

        self.assertEqual(repo.get_loans(), {1: [10], 2: [50]})


