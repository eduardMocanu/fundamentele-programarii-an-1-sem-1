from UI import UI
from lab7_9.repository.in_file.clients_repo import ClientsRepo
from lab7_9.repository.in_file.films_repo import Films_repo
from lab7_9.repository.in_file.loans_repo import Loans_repo
from validators.client_validator import Client_validator
from validators.film_validator import Film_validator
from service.clients_service import Clients_service
from service.loans_service import Lending_service
from service.films_service import Films_service


clients_validators = Client_validator()
films_validators = Film_validator()

clients_repo = ClientsRepo()
films_repo = Films_repo()
lending_repo = Loans_repo()


clients_service = Clients_service(clients_repo, clients_validators)
films_service = Films_service(films_repo, films_validators)
lendings_service = Lending_service(lending_repo, clients_service, films_service)

ui = UI(clients_service, films_service, lendings_service)

ui.run()
