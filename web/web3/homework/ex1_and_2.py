from pymongo import MongoClient

#robo3t
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db=client.c4e
detail_collection = db["posts"]

#4. Create a new document
new_detail = {
    "title": "cuong",
    "content": "nothing",
} # document

client.close()