import time
import pyfiglet
from media import Media
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip
from actors import Actors


print(
    "                                                    Loading")
time.sleep(1)
three = pyfiglet.figlet_format("3")
print(three)
time.sleep(1)
tow = pyfiglet.figlet_format("2")
print(tow)
time.sleep(1)
one = pyfiglet.figlet_format("1")
print(one)
time.sleep(1)

# movie = Media("man of steel", "zack snyder", "7.1",
#               "https://youtu.be/EVsFbdjlpAE", "2013", "henry cavill")
# movie.showinfo()
# movie.download()
movie = []
film = []
series = []
documentary = []
clip = []


def read_data():
    f = open("database.txt", "r")

    for line in f:
        result = line.split(",")
        if line == 0:
            my_obj = Film(result[1], result[2], result[3],
                          result[4], result[5], result[6])
            film.append(my_obj)
            movie.append(film)

        elif line == 1:
            my_obj = Series(result[1], result[2], result[3],
                          result[4], result[5], result[6])
            series.append(my_obj)
            movie.append(series)

        elif line == 2:
            my_obj = Documentary(result[1], result[2], result[3],
                          result[4], result[5], result[6])
            documentary.append(my_obj)
            movie.append(documentary)

        elif line == 3:
            my_obj = Clip(result[1], result[2], result[3],
                          result[4], result[5], result[6])
            clip.append(my_obj)
            movie.append()

    f.close()

read_data()
print(movie)
