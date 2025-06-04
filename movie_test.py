import pytest
from movie import Movie

def test_movie_creation():
    titanic = Movie("Titanic", 1997)
    assert titanic.title == "Titanic"
    assert titanic.year == 1997