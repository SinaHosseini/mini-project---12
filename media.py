import pyfiglet as pf


class Media:
    def __init__(self,type, name, director, imdb, url, duration, casts):
        self.type = type
        self.name = name
        self.director = director
        self.IMBD_score = imdb
        self.url = url
        self.duration = duration
        self.casts = casts

    def showinfo(self):

        print(pf.figlet_format("name is: ", font="epic"))
        print(pf.figlet_format(self.name))
        print(pf.figlet_format("directed by: ", font='epic'))
        print(pf.figlet_format(self.director))
        print(pf.figlet_format("IMBD score is: ", font='epic'))
        print(pf.figlet_format(self.IMBD_score))
        print(pf.figlet_format("year of construction: ", font='epic'))
        print(pf.figlet_format(self.duration))
        ...

    def download(self):
        print(pf.figlet_format("link for watch: "))
        print(self.url, "\n")
        print("👆👆👆👆👆\nclic here")
