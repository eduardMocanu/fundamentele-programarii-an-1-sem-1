from lab7_9.repository.loans_repo import Loans_repo
from lab7_9.service.loans_service import Lending_service
from lab7_9.service.clients_service import Clients_service
from lab7_9.service.films_service import Films_service
from lab7_9.repository.clients_repo import ClientsRepo
from lab7_9.repository.films_repo import Films_repo
from lab7_9.validators.client_validator import Client_validator
from lab7_9.validators.film_validator import Film_validator
from lab7_9.errors.ServiceError import ServiceError
from lab7_9.errors.RepoError import RepoError


def test_add_loan():
    loans_repo = Loans_repo()
    clients_service = Clients_service(ClientsRepo(), Client_validator())
    films_service = Films_service(Films_repo(), Film_validator())
    lending_service = Lending_service(loans_repo, clients_service, films_service)

    clients_service.add_client(1, "Edy", "1234567890123")
    films_service.add_film(10, "Film X", "Descriere", "test")

    # adăugăm împrumutul
    lending_service.add_loan(1, 10)
    assert loans_repo.get_loans() == {1: [10]}

    # încercăm să adăugăm același împrumut → RepoError
    try:
        lending_service.add_loan(1, 10)
        assert False, "RepoError should have been raised"
    except RepoError:
        assert True

    # client inexistent → ServiceError
    try:
        lending_service.add_loan(999, 10)
        assert False, "ServiceError should have been raised"
    except ServiceError:
        assert True

    # film inexistent → ServiceError
    try:
        lending_service.add_loan(1, 999)
        assert False, "ServiceError should have been raised"
    except ServiceError:
        assert True


def test_remove_loan():
    loans_repo = Loans_repo()
    clients_service = Clients_service(ClientsRepo(), Client_validator())
    films_service = Films_service(Films_repo(), Film_validator())
    lending_service = Lending_service(loans_repo, clients_service, films_service)

    clients_service.add_client(1, "Edy", "1234567890123")
    films_service.add_film(10, "Film X", "Descriere", "test")

    lending_service.add_loan(1, 10)
    lending_service.remove_loan(1, 10)
    assert loans_repo.get_loans() == {1: []}

    # încercăm să ștergem un împrumut inexistent → RepoError
    try:
        lending_service.remove_loan(1, 10)
        assert False, "RepoError should have been raised"
    except RepoError:
        assert True

    # client inexistent → ServiceError
    try:
        lending_service.remove_loan(999, 10)
        assert False, "ServiceError should have been raised"
    except ServiceError:
        assert True

    # film inexistent → ServiceError
    try:
        lending_service.remove_loan(1, 999)
        assert False, "ServiceError should have been raised"
    except ServiceError:
        assert True


def test_clients_loaned_films_sorted():
    loans_repo = Loans_repo()
    clients_service = Clients_service(ClientsRepo(), Client_validator())
    films_service = Films_service(Films_repo(), Film_validator())
    lending_service = Lending_service(loans_repo, clients_service, films_service)

    clients_service.add_client(1, "Alex", "1234567890123")
    clients_service.add_client(2, "Edy", "1234567890129")
    films_service.add_film(10, "A", "desc", "test")
    films_service.add_film(20, "B", "desc", "test")

    lending_service.add_loan(1, 10)
    lending_service.add_loan(2, 10)
    lending_service.add_loan(2, 20)

    result = lending_service.clients_loaned_films_sorted()
    assert result == [["Alex", 1], ["Edy", 2]]


def test_most_loaned_films():
    loans_repo = Loans_repo()
    clients_service = Clients_service(ClientsRepo(), Client_validator())
    films_service = Films_service(Films_repo(), Film_validator())
    lending_service = Lending_service(loans_repo, clients_service, films_service)

    clients_service.add_client(1, "Edy", "1234567890123")
    clients_service.add_client(2, "Alex", "1234567890129")
    films_service.add_film(10, "Film X", "desc", "test")
    films_service.add_film(20, "Film Y", "desc", "test")

    lending_service.add_loan(1, 10)
    lending_service.add_loan(2, 10)
    lending_service.add_loan(1, 20)

    result = lending_service.most_loaned_films()
    assert len(result) == 1
    assert result[0].get_titlu() == "Film X"


def test_top_30_clients():
    loans_repo = Loans_repo()
    clients_service = Clients_service(ClientsRepo(), Client_validator())
    films_service = Films_service(Films_repo(), Film_validator())
    lending_service = Lending_service(loans_repo, clients_service, films_service)

    clients_service.add_client(1, "Edy", "1111111111111")
    clients_service.add_client(2, "Alex", "2222222222222")
    clients_service.add_client(3, "Mihai", "3333333333333")
    films_service.add_film(10, "A", "desc", "test")
    films_service.add_film(20, "B", "desc", "test")

    lending_service.add_loan(1, 10)
    lending_service.add_loan(1, 20)
    lending_service.add_loan(2, 10)

    result = lending_service.top_30_clients()
    assert result == [["Edy", 2]]


def tests_lending_service():
    test_add_loan()
    test_remove_loan()
    test_clients_loaned_films_sorted()
    test_most_loaned_films()
    test_top_30_clients()