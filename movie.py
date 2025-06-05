import os
import time
import requests

class Movie():
    TMDB_API_KEY = os.getenv("TMDB_API_KEY")
    TMDB_BASE_URL = "https://api.themoviedb.org/3"

    def __init__(self, title, year, letterboxd_uri):
        self.title = title
        self.year = year
        self.letterboxd_uri = letterboxd_uri
        self.tmdb_id = None
        self.directors = []
        self.directors_genders = []
    
    def fetch_tmdb_id(self):
        """
        Calls TMDB API to get movie's id by getting the first result in a search by title and year.
        """
        movie_response = requests.get(f"{Movie.TMDB_BASE_URL}/search/movie?query={self.title}&year={self.year}&api_key={Movie.TMDB_API_KEY}")
        if movie_response.status_code == 429:
            print("Rate limit exceeded, sleeping 10 seconds")
            time.sleep(10)
        movie_json = movie_response.json()
        if "results" in movie_json and movie_json["total_results"] > 0: # Manages in case no results are found
            self.tmdb_id = movie_json["results"][0]["id"]
        else:
            print(f"No results for movie: {self.title}")
            self.tmdb_id = None

    def fetch_directors_genders(self):
        """
        Calls TMDB API to get the directors of the movie and their gender.
        Updates self.directors
        """
        movie_response = requests.get(f"{Movie.TMDB_BASE_URL}/movie/{self.tmdb_id}/credits?api_key={Movie.TMDB_API_KEY}")

        movie_json = movie_response.json()
        if movie_response.status_code == 429:
            print("Rate limit exceeded, sleeping 10 seconds")
            time.sleep(10)
        
        self.directors = [member for member in movie_json["crew"] if member["job"] == "Director"]
        self.directors_genders = [director["gender"] for director in self.directors]

    @property
    def is_directed_by_woman(self):
        if len(self.directors_genders) < 1:
            return self.directors_genders[0] == 1
        else: 
            return any(gender == 1 for gender in self.directors_genders)