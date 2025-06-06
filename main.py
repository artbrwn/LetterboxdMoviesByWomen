import csv
from dotenv import load_dotenv
import time
load_dotenv()
from movie import Movie


"""
TODO:
Capture unfound films and display them
capture unidentified directors and display them
    - Allow to identify manually those movies.
Give the possibility to chose between watched and watchlist, and in watchlist give the option
to export as a csv.

"""

def get_data():
    """
    Reads the csv file and returns a list with the data of the movie required to create the Movie object.
    """
    with open("data/watched.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)
        # Appends all the watched movies to a list watched_movies as a tuple name, release year
        watched_movies = []
        for line in csv_reader:
            watched_movies.append((line[1], line[2], line[3]))
    return watched_movies

def analyze_movies(watched_movies):
    """
    Analyzes a list of watched movies and categorizes them based on their directors' gender.

    For each movie in the input list, this function:
    - Creates a Movie object using the title, year, and Letterboxd URI.
    - Calls the property `is_directed_by_woman`, which internally fetches and updates:
        - `tmdb_id`: the TMDB identifier for the movie,
        - `directors_genders`: a list of gender values for each director,
        - `is_directed_by_woman`: a boolean indicating if all identified directors are women.
    - Appends the movie to one of the following lists:
        - `by_women`: if directed by women,
        - `not_found`: if the movie was not found on TMDB,
        - `unidentified`: if the movie was found but no gender could be determined for its directors.

    Args:
        watched_movies (list of tuples): Each tuple contains (title, year, letterboxd_uri) of a movie.

    Returns:
        dict: A dictionary with the following keys:
            - "by_women": list of Movie objects directed by women,
            - "not_found": list of Movie objects not found on TMDB,
            - "unidentified": list of Movie objects with unknown director genders,
            - "total": total number of movies analyzed.
    
    """
    
    watched_movies_by_women = []
    not_found_movies = []
    unidentified_movies = []

    for element in watched_movies:
        movie = Movie(element[0], element[1], element[2])
        print(f"Analyzing {watched_movies.index(element) + 1} of {len(watched_movies)}: {movie.title}")

        if movie.is_directed_by_woman:
            watched_movies_by_women.append(movie)
            print(f"{movie.title} is directed by women")
        else:
            if movie.tmdb_id == None:
                not_found_movies.append(movie)
            elif movie.directors_genders == []:
                unidentified_movies.append(movie)
            
        time.sleep(0.05)

    return {
        "by_women": watched_movies_by_women,
        "not_found": not_found_movies,
        "unidentified": unidentified_movies,
        "total": len(watched_movies)
    }


def print_results(results):
    by_women = results["by_women"]
    not_found = results["not_found"]
    unidentified = results["unidentified"]
    total = results["total"]
    # PRINT RESULTS
    percentage_by_women = (len(by_women) *100) / total
    print(f"You've watched {len(by_women)} movies directed by women out of {total} movies in total. That is a {percentage_by_women:.2f}%.")
    print(f"{len(not_found)} films not found. The movies we couldn't find were are:")
    for element in not_found:
        print(f"{element.title}.")
    print(f"The movies we couldn't identify are:")
    for element in unidentified:
        print(f"{element.title} by {element.directors[0]["name"]}")
    print(f"Your watched movies by women are:")
    for element in by_women:
        print(f"{element.title} by {element.directors[0]["name"]}")


def export_results(results):
    """
    Exports the list of movies directed by women to a CSV file compatible with Letterboxd.

    This function takes the dictionary returned by `analyze_movies`, extracts the movies
    categorized as directed by women (`results["by_women"]`), and writes their title, year,
    and Letterboxd URI to a CSV file named `watchlist_by_women.csv`.

    The resulting file can be imported directly into a Letterboxd watchlist.

    """
    with open("watchlist_by_women.csv", "w", newline="") as csvfile:
        fieldnames = ["Name","Year","Letterboxd URI"]
        
        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        thewriter.writeheader()

        for movie in results["by_women"]:
            thewriter.writerow({"Name": movie.title, "Year": movie.year, "Letterboxd URI": movie.letterboxd_uri})

    print("Your data has been exported, you can now import it to Letterboxd.")

def main():
    watched_movies = get_data()
    analysis_result = analyze_movies(watched_movies)
    print_results(analysis_result)
    export_results(analysis_result)


if __name__ == "__main__":
    main()