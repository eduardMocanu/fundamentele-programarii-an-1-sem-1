from lab7_9.validators_tests.test_client_validator import tests_client_validator
from lab7_9.services_tests.test_service_clients import tests_service_clients
from lab7_9.repository_tests.test_clients_repo import test_clients_repo
from lab7_9.validators_tests.test_films_validator import tests_film_validator
from lab7_9.services_tests.test_service_films import tests_service_films
from lab7_9.repository_tests.test_films_repo import test_films_repo
from lab7_9.repository_tests.test_loans_repo import tests_loans_repo
from lab7_9.services_tests.test_service_loans import tests_lending_service


def test():
    tests_lending_service()
    tests_service_clients()
    test_clients_repo()
    tests_client_validator()
    tests_film_validator()
    tests_service_films()
    test_films_repo()
    tests_loans_repo()