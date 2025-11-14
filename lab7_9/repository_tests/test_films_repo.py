from lab7_9.model.Film import Film
from lab7_9.repository.films_repo import Films_repo


def test_add_film():
    repo = Films_repo()
    film = Film(1, "Title", "Desc", "Gen")
    repo.add_film(film)
    assert film in repo.get_all_films()


def test_remove_film():
    repo = Films_repo()
    film = Film(1, "Title", "Desc", "Gen")
    repo.add_film(film)
    repo.remove_film(film)
    assert film not in repo.get_all_films()


def test_modify_film():
    repo = Films_repo()
    film_old = Film(1, "OldTitle", "OldDesc", "OldGen")
    repo.add_film(film_old)

    film_new = Film(2, "NewTitle", "NewDesc", "NewGen")
    repo.modify_film(film_old.get_id(), film_new)

    modified = repo.find_film_by_id(2)

    assert modified is not None
    assert modified.get_titlu() == "NewTitle"
    assert modified.get_descriere() == "NewDesc"
    assert modified.get_gen() == "NewGen"


def test_find_film_by_id():
    repo = Films_repo()
    film = Film(10, "ABC", "DEF", "XYZ")
    repo.add_film(film)

    assert repo.find_film_by_id(10) == film
    assert repo.find_film_by_id(99) is None


def test_get_all_films():
    repo = Films_repo()
    f1 = Film(1, "T1", "D1", "G1")
    f2 = Film(2, "T2", "D2", "G2")
    repo.add_film(f1)
    repo.add_film(f2)

    films = repo.get_all_films()
    assert f1 in films
    assert f2 in films


def test_films_repo():
    test_add_film()
    test_remove_film()
    test_modify_film()
    test_find_film_by_id()
    test_get_all_films()