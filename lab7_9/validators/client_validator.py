from lab7_9.errors.ServiceError import ServiceError


class Client_validator:
    """
    Validator pentru obiectele Client.

    Funcționalități principale:
    - verifică dacă un client este valid
    - verifică validitatea unui ID de client
    """

    def verify_client(self, client):
        """
        Verifică dacă un obiect Client este valid.

        Parametri:
        - client: obiectul Client de verificat

        Condiții de validitate:
        - clientul nu trebuie să fie None
        - ID-ul trebuie să fie > 0
        - numele nu trebuie să fie gol
        - CNP-ul trebuie să aibă exact 13 caractere

        Aruncă:
        - ServiceError cu mesaj corespunzător dacă o condiție nu este îndeplinită
        """
        if client is None:
            raise ServiceError("client invalid")
        if client.get_id() <= 0:
            raise ServiceError("id invalid")
        if len(client.get_nume()) == 0:
            raise ServiceError("nume invalid")
        if len(client.get_CNP()) != 13:
            raise ServiceError("CNP invalid")

    def id_verification(self, client_id):
        """
        Verifică dacă un ID de client este valid.

        Parametri:
        - client_id: ID-ul de verificat

        Condiție:
        - ID-ul trebuie să fie > 0

        Aruncă:
        - ServiceError dacă ID-ul nu este valid
        """
        if client_id <= 0:
            raise ServiceError("id invalid")