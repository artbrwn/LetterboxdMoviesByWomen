from movie import Movie

def test_movie_creation():
    titanic = Movie("Titanic", "1997", "https://boxd.it/2a2k")
    assert titanic.title == "Titanic"
    assert titanic.year == "1997"
    titanic.fetch_tmdb_id()
    assert titanic.tmdb_id == 597