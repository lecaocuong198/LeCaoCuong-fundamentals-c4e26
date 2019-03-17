from db import food_collection,user_collection
from bson import ObjectId

def add_food(name,price):
    new_food = {
        "name" :name,
        "price": price,
    }
    food_collection.insert_one(new_food)

def add_user(name,password):
    new_user = {
        "name" :name,
        "password": password,
    }
    user_collection.insert_one(new_user)



def get(query):
    food_list= food_collection.find(query)
    return food_list

def get_by_id(id):
    f = food_collection.find_one({ "_id": ObjectId(id)})
    return f

def delete_by_id(id):
    f =  food_collection.delete_one({"_id": ObjectId(id)})

def update_by_id(id,updater,nd,up,dp):
    query = {"_id": ObjectId(id)}
    updater = {dp: {nd: up}}#inc,$dec,$set,$unset
    food_collection.find_one_and_update(query,updater)

def find_by_username(username):
    f = user_collection.find_one({"name": username})
    return f

if __name__=="__main__":
    print(find_by_username('admin'))

    # print(*get({}))
    # query = {"_id": ObjectId("5c812331ce5dc41af0b2c49b")}
    # updater = {"$set": {"price": 50000}}#inc,$dec,$set,$unset
    # food_collection.find_one_and_update(query,updater)
    # print(*get({}),sep = "\n")
    
    # f = food_collection.find_one({ "_id": ObjectId("5c8124d8ce5dc415e0340b17")})
    # print(f)
    # food_collection.delete_one({"_id": ObjectId("5c8124d8ce5dc415e0340b17")})
    # f = get_by_id("5c8124d8ce5dc415e0340b17")
    # if f != None:
    #     print(f['name'])
    # else:
    #     print("Not found")
    # for food in get({  "price ": { "$gte": 25000}}):
    #     print(food)