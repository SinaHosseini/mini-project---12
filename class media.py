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
media = []


def read_data():
    f = open("episode12/database.txt", "r")

    for line in f:
        media = line.split("\n")
        for i in range(len(media)):
            split = media[i].split(",")
            if split[0] == "film":
                media.append(Film(split[0], split[1], split[2], split[3], split[4], split[5], split[6]))

            elif split[1] == "series":
                media.append(Series(split[0], split[1], split[2], split[3], split[4], split[5], split[6]))

            elif split[2] == "documentary":
                media.append(Documentary(split[0], split[1], split[2], split[3], split[4], split[5], split[6]))

            elif split[3] == "clip":
                media.append(Clip(split[0], split[1], split[2], split[3], split[4], split[5], split[6]))

            return media

    f.close()


media = read_data()
print(media)
