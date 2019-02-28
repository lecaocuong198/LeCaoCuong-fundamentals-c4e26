from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

n = input("Nhap vao dia diem? ")
url="https://wind.waqi.info/nsearch/full/"+n+"?n=4"
conn=urlopen(url)
raw_data=conn.read()
page_content=raw_data.decode("utf8")
soup=BeautifulSoup(page_content,"html.parser")
y = json.loads(page_content)
result = y['results']
time = result[0]["s"]["t"]
aqi = result[0]["s"]["a"]

kq = f"Location: {y['term']}\nAqi: {aqi}\nTime: {time}"
print(kq)



