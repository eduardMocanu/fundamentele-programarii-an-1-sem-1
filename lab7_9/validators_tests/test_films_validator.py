from lab7_9.errors.ServiceError import ServiceError
from lab7_9.model.Film import Film
from lab7_9.validators.film_validator import Film_validator


def test_verify_film():
    film_validator = Film_validator()
    film = Film(1, "Title", "Description", "Gen")
    assert film_validator.verify_film(film) is None

    try:
        film_validator.verify_film(Film(1, "", "Desc", "Gen"))
        assert False
    except ServiceError:
        assert True

    try:
        film_validator.verify_film(Film(1, "Title", "", "Gen"))
        assert False
    except ServiceError:
        assert True

    try:
        film_validator.verify_film(Film(1, "Title", "Desc", ""))
        assert False
    except ServiceError:
        assert True

    try:
        film_validator.verify_film(Film(-5, "Title", "Desc", "Gen"))
        assert False
    except ServiceError:
        assert True

    try:
        film_validator.verify_film(None)
        assert False
    except ServiceError:
        assert True


def test_id_verificator():
    film_validator = Film_validator()
    assert film_validator.id_verificator(1) is None

    try:
        film_validator.id_verificator(0)
        assert False
    except ServiceError:
        assert True

    try:
        film_validator.id_verificator(-10)
        assert False
    except ServiceError:
        assert True


def tests_film_validator():
    test_verify_film()
    test_id_verificator()