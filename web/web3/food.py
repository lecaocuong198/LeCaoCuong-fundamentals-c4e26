from db import food_collection,close

def add_food(name,price):
# while True:

    # if name == "exit" or price == 0:
    #     close()
    #     break
    # else:
    new_food = {
        "name" :name,
        "price": price,
    }
    food_collection.insert_one(new_food)
    close
    return new_food



def get():
    food_list= food_collection.find()
    return food_list

if __name__=="__main__":


    food_list= food_collection.find(
        {
            "price": {"$gte": 12000,}
        }
    ) #lazy loading


    for food in food_list:
            print(food['name'])
            print(food['price'])


