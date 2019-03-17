from pymongo import MongoClient

uri = "mongodb+srv://admin:admin1@cluster0-ehqpe.mongodb.net/test?retryWrites=trueW"
# Connect
client = MongoClient(uri)

# Get database
db = client.test

#3.Get collection
food_collection = db["food"] #collection

user_collection = db["user"]


#4. Create a new document
# new_food = {
#     "name": "bun ca",
#     "price": 30000,
# } # document

# #5. Insert new document into collection
# food_collection.insert_one(new_food)



#6. Close connection
def close():
    client.close()