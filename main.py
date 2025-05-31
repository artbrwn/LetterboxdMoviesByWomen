import csv

with open("data/watched.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    watched_movies = []
    for line in csv_reader:
        watched_movies.append(line[1])

watched_movies_by_women = []

for movie in watched_movies:
    if is_directed_by_woman(movie):
        watched_movies_by_women.append(movie)

def is_directed_by_woman(m):
    pass
