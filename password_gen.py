import pdb
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import random


def standardize(snt):
    return "".join([l.lower() for l in snt if l.isalpha()])


while True:
    try:
        song = input("Song: ")
        artist = input("Artist: ")
        url = "https://www.azlyrics.com/lyrics/" + \
               standardize(artist) + \
               "/" + \
               standardize(song) + \
               ".html"
        page = urlopen(url).read()
        break
    except HTTPError:
        print("Sorry, try again")
        continue

html = BeautifulSoup(page, "html5lib")
text = html.get_text()

# start = text.find('"' + song + '" lyrics')
starts = [m.end() for m in re.finditer(song, text)]
end = text.find("if  ( /Android")

text = text[starts[3]:end].strip()
text_list = text.split("\n")
text_list = [line for line in text_list if not (line == "" or line[0] == "]")]

random.seed(len(song) + len(artist))
line = text_list[random.randint(0, len(text_list))].split(" ")
r1 = random.randint(0, len(line)-4)
words = line[r1:r1+4]
r2 = random.randint(0, 3)
words[r2] = words[r2].upper()
words = "".join(words)

print(words)
