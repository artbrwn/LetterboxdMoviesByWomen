import csv
import requests
from dotenv import load_dotenv
import os
import time


"""
TODO:
Capture movies by women and display them
Change uncaptured for not_found
Review logic for uncaptureds
Capture uncaptured films and display them

"""

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
    """
    It gets a tupple (title, year) and it returns the tmdb id of that movie.
    """
    movie_response = requests.get(f"{TMDB_BASE_URL}/search/movie?query={lett_movie[0]}&year={lett_movie[1]}&api_key={TMDB_API_KEY}")
    if movie_response.status_code == 429:
        print("Rate limit exceeded, sleeping 10 seconds")
        time.sleep(10)
    movie_json = movie_response.json()
    if "results" in movie_json and movie_json["total_results"] > 0: # Manages in case no results are found
        movie_id = movie_json["results"][0]["id"]
        return movie_id
    else:
        print(f"No results for movie: {lett_movie}")
        return None

def get_gender_from_movie(movie_id):
    """
    It gets an id of a movie and returns True if at least one of the directors is a woman
    """
    if movie_id == None:
        global unidentified_movies
        unidentified_movies += 1
        return None
    
    movie_response = requests.get(f"{TMDB_BASE_URL}/movie/{movie_id}/credits?api_key={TMDB_API_KEY}")

    movie_json = movie_response.json()
    if movie_response.status_code == 429:
        print("Rate limit exceeded, sleeping 10 seconds")
        time.sleep(10)
    directors = [member for member in movie_json["crew"] if member["job"] == "Director"]
    directors_genders = [director["gender"] for director in directors]
    return directors_genders

def is_directed_by_woman(directors_genders):
    if directors_genders == None:
        return None
    # if it has one director
    if len(directors_genders) == 1:
        # if its a woman
        if directors_genders[0] == 1:
            return True
            # Returns True
        elif directors_genders[0] == 2:
            return False
        else:
            # TODO: capture nonbinary or others.
            return False
    else:
        # iterates
        # if one is a woman
        return any(gender == 1 for gender in directors_genders)

# Iterates watched_movies, applies is_directed_by_woman() and appends to watched_movies_by_women if True.
n_of_movies_total = len(watched_movies)
watched_movies_by_women = []
uncaptured_movies = 0
unidentified_movies = 0

for movie in watched_movies:
    print(f"Analyzing {watched_movies.index(movie)} of {n_of_movies_total}: {movie[0]}")
    movie_id = get_movie_id_from_lett(movie)
    if movie_id:
        movie_gender = get_gender_from_movie(movie_id)
        if movie_gender:
            if is_directed_by_woman(movie_gender):
                watched_movies_by_women.append(movie)
    
    time.sleep(0.05)

n_of_movies_by_women = len(watched_movies_by_women)
percentage_by_women = (n_of_movies_by_women *100) / n_of_movies_total


# PRINT RESULTS
print(f"You've watched {n_of_movies_by_women} movies directed by women out of {n_of_movies_total} movies in total. That is a {percentage_by_women:.2f}%.")
print(f"{uncaptured_movies} uncaptured films.")
