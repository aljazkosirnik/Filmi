class AllMovies:
    def __init__(self, id_s, poster_path, title, vote_average, release_date):
        self.id_s = id_s
        self.poster_path = poster_path
        self.title = title
        self.vote_average = vote_average
        self.release_date = release_date


class AllShows:
    def __init__(self, id_s, poster_path, title, vote_average, release_date):
        self.id_s = id_s
        self.poster_path = poster_path
        self.title = title
        self.vote_average = vote_average
        self.release_date = release_date


class Trending:
    def __init__(self, id_s, poster_path, title, vote_average, release_date, url):
        self.id_s = id_s
        self.poster_path = poster_path
        self.title = title
        self.vote_average = vote_average
        self.release_date = release_date
        self.url = url
