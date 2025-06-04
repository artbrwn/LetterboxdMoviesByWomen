class Movie():
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.tmdb_id = None
        self.directors = []
        self.directors_genders = []