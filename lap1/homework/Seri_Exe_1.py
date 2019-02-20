from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

raw_data = conn.read()
pageContent = raw_data.decode("utf8")
soup = BeautifulSoup(pageContent,"html.parser")


ul = soup.find("ul","")
li_list = ul.find_all('li')

new_list = []
options = {
    "default_search": "ytsearch",
    "max_dowload": 100,
    "format":"bestaudio/audio",
}
dl = YoutubeDL(options)
for li in li_list:
    h3 = li.h3
    a = h3.a
    title = a.string
    h4 = li.h4
    a1 = h4.a
    artist = a1.string
    news = {
        "title":title,
        "artist":artist,
    }
    key = title
    print(key)
    dl.download([key])
    new_list.append(news)
pyexcel.save_as(records=new_list, dest_file_name="itunes.xls")






