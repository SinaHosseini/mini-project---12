from media import Media


class Documentary(Media):
    def __init__(self, type, name, director, imdb, url, duration, casts):
        super().__init__(type, name, director, imdb, url, duration, casts)
