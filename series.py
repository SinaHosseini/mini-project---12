from media import Media

class Series(Media):
    def __init__(self, name, director, imdb, url, duration, casts, sessions):
        super().__init__(name, director, imdb, url, duration, casts)
        self.sessions = sessions