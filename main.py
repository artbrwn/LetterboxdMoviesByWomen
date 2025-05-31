import csv
import requests
from dotenv import load_dotenv
import os
import json

# API
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"
# GET DATA
# Opens the watched.csv file in Data
with open("data/watched.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    # Appends all the watched movies to a list watched_movies as a tuple name, release year
    watched_movies = []
    for line in csv_reader:
        watched_movies.append((line[1], line[3]))

# PROCESS DATA
def get_movie_id_from_lett(lett_movie):
    return "835504"

def is_directed_by_woman(lett_movie): # PRUEBA, CAMBIAR NOMBRE A  is_directed_by_woman
    # get the ID of the movie from lett_movie
    movie_id = get_movie_id_from_lett(lett_movie)
    # search the movie in tmdb
    movie_response = requests.get(f"{TMDB_BASE_URL}/movie/{movie_id}/credits?api_key={TMDB_API_KEY}")
    movie_json = json.loads(movie_response.text)

    directors = [member for member in movie_json["crew"] if member["job"] == "Director"]
    directors_genders = [director["gender"] for director in directors]
    # if it has one director
    if len(directors_genders) == 1:
        # if its a woman
        if directors_genders[0] == 1:
            return True
            # Returns True
        else:
            return False
    else:
        # iterates
        # if one is a woman
        return any(gender == 1 for gender in directors_genders)

    
    # If nothing happens return False

# Iterates watched_movies, applies is_directed_by_woman() and appends to watched_movies_by_women if True.
watched_movies_by_women = []

for movie in watched_movies:
    if is_directed_by_woman(movie):
        watched_movies_by_women.append(movie)

n_of_movies_total = len(watched_movies)
n_of_movies_by_women = len(watched_movies_by_women)
percentage_by_women = (n_of_movies_by_women *100) / n_of_movies_total

# PRINT RESULTS
print(f"You've watched {n_of_movies_by_women} movies directed by women out of {n_of_movies_total} movies in total. That is a {percentage_by_women}%.")