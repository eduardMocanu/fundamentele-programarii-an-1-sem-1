from lab7_9.service.films_service import Films_service
from lab7_9.errors.ServiceError import ServiceError
from lab7_9.repository.films_repo import Films_repo
from lab7_9.validators.film_validator import Film_validator

def test_add_film():
    films_repo = Films_repo()
    films_validator = Film_validator()
    films_service = Films_service(films_repo, films_validator)
    try:
        films_service.add_film(1, "", "Desc", "Gen")
        assert False, "ServiceError should have been raised"
    except ServiceError:
        assert True

    films_service.add_film(1, "Title", "Desc", "Gen")

    films = films_service.get_films()
    assert any(
        f.get_id() == 1 and f.get_titlu() == "Title"
        for f in films
    ), "Film should be stored"


def test_remove_film_by_id():
    films_repo = Films_repo()
    films_validator = Film_validator()
    films_service = Films_service(films_repo, films_validator)

    films_service.add_film(1, "Test", "Desc", "Gen")

    films_service.remove_film_by_id(1)
    assert all(f.get_id() != 1 for f in films_service.get_films())
    try:
        films_service.remove_film_by_id(999)
        assert False, "ServiceError should have been raised"
    except ServiceError:
        assert True


def test_modify_film():
    films_repo = Films_repo()
    films_validator = Film_validator()
    films_service = Films_service(films_repo, films_validator)

    films_service.add_film(1, "Old", "OldDesc", "OldGen")

    films_service.modify_film(1, 2, "New", "NewDesc", "NewGen")

    films = films_service.get_films()
    modified = None
    for f in films:
        if f.get_id() == 2:
            modified = f
            break

    assert modified is not None, "Film should exist"
    assert modified.get_titlu() == "New"
    assert modified.get_descriere() == "NewDesc"
    assert modified.get_gen() == "NewGen"

    try:
        films_service.modify_film(999, 10, "X", "Y", "Z")
        assert False, "ServiceError should have been raised"
    except ServiceError:
        assert True


def test_search_film_by_id():
    films_repo = Films_repo()
    films_validator = Film_validator()
    films_service = Films_service(films_repo, films_validator)

    films_service.add_film(10, "Movie", "Desc", "Gen")

    found = films_service.search_film_by_id(10)
    assert found.get_id() == 10
    assert found.get_titlu() == "Movie"
    assert found.get_descriere() == "Desc"

    try:
        films_service.search_film_by_id(999)
        assert False, "ServiceError should have been raised"
    except ServiceError:
        assert True


def test_get_films():
    films_repo = Films_repo()
    films_validator = Film_validator()
    films_service = Films_service(films_repo, films_validator)

    assert films_service.get_films() == []

    films_service.add_film(1, "A", "D1", "G1")
    films_service.add_film(2, "B", "D2", "G2")

    films = films_service.get_films()
    assert any(f.get_id() == 1 for f in films)
    assert any(f.get_id() == 2 for f in films)
    assert len(films) == 2


def tests_service_films():
    test_add_film()
    test_remove_film_by_id()
    test_modify_film()
    test_search_film_by_id()
    test_get_films()