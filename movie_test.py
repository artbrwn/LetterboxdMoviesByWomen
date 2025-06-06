from movie import Movie

def test_movie_creation():
    titanic = Movie("Titanic", "1997", "https://boxd.it/2a2k", "2023-06-12")
    assert titanic.title == "Titanic"
    assert titanic.year == "1997"
    assert titanic.watch_date == "2023-06-12"
    titanic.fetch_tmdb_id()
    assert titanic.tmdb_id == 597