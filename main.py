import csv
from dotenv import load_dotenv
import time
load_dotenv()
from movie import Movie


"""
TODO:
Capture unfound films and display them
capture unidentified directors and display them
Give the possibility to chose between watched and watchlist, and in watchlist give the option
    to export as a csv.
Change logic to make objects for movies, in order to be able to display movies unidentified and their directors,
    movies directed by women and their directors, and other options.
"""

# GET DATA
# Opens the watched.csv file in Data
with open("data/watched.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    # Appends all the watched movies to a list watched_movies as a tuple name, release year
    watched_movies = []
    for line in csv_reader:
        watched_movies.append((line[1], line[2], line[3]))

# Iterates watched_movies, applies is_directed_by_woman() and appends to watched_movies_by_women if True.
n_of_movies_total = len(watched_movies)
watched_movies_by_women = []
not_found_movies = 0
unidentified_movies = 0

for element in watched_movies:
    movie = Movie(element[0], element[1], element[2])
    print(f"Analyzing {watched_movies.index(element) + 1} of {n_of_movies_total}: {movie.title}")
    movie.fetch_tmdb_id()
    if movie.tmdb_id:
        movie.fetch_directors_genders()
        if movie.directors_genders:
            if movie.is_directed_by_woman:
                watched_movies_by_women.append(movie)
                print(f"{movie.title} is directed by women")

    time.sleep(0.05)

n_of_movies_by_women = len(watched_movies_by_women)
percentage_by_women = (n_of_movies_by_women *100) / n_of_movies_total


# PRINT RESULTS
print(f"You've watched {n_of_movies_by_women} movies directed by women out of {n_of_movies_total} movies in total. That is a {percentage_by_women:.2f}%.")
print(f"{not_found_movies} films not found.")
print(f"{unidentified_movies} films not identified.")
print(f"Your watched movies by women are:")
for element in watched_movies_by_women:
    print(f"{element.title} by {element.directors[0]["name"]}")

# EXPORT RESULTS AS CSV

with open("watchlist_by_women.csv", "w", newline="") as csvfile:
    fieldnames = ["Name","Year","Letterboxd URI"]
    
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

    thewriter.writeheader()

    for movie in watched_movies_by_women:
        thewriter.writerow({"Name": movie.title, "Year": movie.year, "Letterboxd URI": movie.letterboxd_uri})

print("Your data has been exported, you can now import it to Letterboxd.")