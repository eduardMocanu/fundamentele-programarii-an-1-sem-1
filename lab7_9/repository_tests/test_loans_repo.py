from lab7_9.repository.loans_repo import Loans_repo
from lab7_9.errors.RepoError import RepoError


def test_add_loan_new_client():
    repo = Loans_repo()
    repo.add_loan(1, 10)
    loans = repo.get_loans()
    assert 1 in loans
    assert loans[1] == [10]


def test_add_loan_existing_client_new_film():
    repo = Loans_repo()
    repo.add_loan(1, 10)
    repo.add_loan(1, 20)
    loans = repo.get_loans()
    assert loans[1] == [10, 20]


def test_add_loan_same_film_raises():
    repo = Loans_repo()
    repo.add_loan(1, 10)
    try:
        repo.add_loan(1, 10)
        assert False, "Trebuia să ridice RepoError"
    except RepoError:
        assert True


def test_remove_loan_valid():
    repo = Loans_repo()
    repo.add_loan(1, 10)
    repo.add_loan(1, 20)
    repo.remove_loan(1, 10)
    loans = repo.get_loans()
    assert loans[1] == [20]


def test_remove_loan_nonexistent_client():
    repo = Loans_repo()
    try:
        repo.remove_loan(1, 10)
        assert False, "Trebuia să ridice RepoError"
    except RepoError:
        assert True


def test_remove_loan_film_not_borrowed():
    repo = Loans_repo()
    repo.add_loan(1, 10)
    try:
        repo.remove_loan(1, 20)
        assert False, "Trebuia să ridice RepoError"
    except RepoError:
        assert True


def test_get_loans_structure():
    repo = Loans_repo()
    repo.add_loan(1, 10)
    repo.add_loan(2, 50)
    loans = repo.get_loans()
    assert loans == {1: [10], 2: [50]}


def tests_loans_repo():
    test_get_loans_structure()
    test_remove_loan_film_not_borrowed()
    test_remove_loan_nonexistent_client()
    test_remove_loan_valid()
    test_add_loan_same_film_raises()
    test_add_loan_existing_client_new_film()
    test_add_loan_new_client()