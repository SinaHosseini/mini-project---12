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

movie = Media("man of steel", "zack snyder", "7.1",
              "https://youtu.be/EVsFbdjlpAE", "2013", "henry cavill")
movie.showinfo()
movie.download()
