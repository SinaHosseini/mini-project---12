from media import Media


class Series(Media):
    def __init__(self, type, name, director, imdb, url, duration, casts, sessions):
        super().__init__(type, name, director, imdb, url, duration, casts)
        self.sessions = sessions
