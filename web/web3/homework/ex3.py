from ex1_and_2 import db
from pymongo import MongoClient
import matplotlib.pyplot as plt

cus_collection = db["customers"]

list_cus = cus_collection.find()

ev = 0
wom = 0
ads = 0
for cus in list_cus:
    if cus["ref"]=="events":
        ev+=1
    if cus["ref"]=="wom":
        wom +=1
    if cus["ref"]=="ads": 
        ads +=1

labels = 'events', 'wom', 'ads'
sizes = [ev,wom,ads]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.1, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
