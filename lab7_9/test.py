from .validators_tests.test_client_validator import tests_client_validator
from .services_tests.test_service_clients import tests_service_clients
from .repos_tests.test_clients_repo import test_clients_repo

def test():
    tests_service_clients()
    test_clients_repo()
    tests_client_validator()