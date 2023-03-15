from media import Media

class Clip(Media):
    def __init__(self, name, director, imdb, url, duration, casts):
        super().__init__(name, director, imdb, url, duration, casts)
