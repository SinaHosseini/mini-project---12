class Media:
    def __init__(self, name, director, imdb, url, duration, casts):
        self.name = name
        self.director = director
        self.IMBD_score = imdb
        self.url = url
        self.duration = duration
        self.casts = casts

    def showinfo(self):
        ...

    def download(self):
        ...
