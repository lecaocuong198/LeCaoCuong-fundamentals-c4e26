from ex4 import river_collection


if __name__=="__main__":

    America= []
    America_list = river_collection.find(
        {
            "continent": {"$eq": "S. America",},"length": {"$lt": 1000}
        }
        # {
        #     "length": {"$lt": 1000}
        # }
    )
    for country in America_list:
        new_list = {
            "name" : country["name"],
            "continent": country["continent"],
            "length": country["length"]
        }
        America.append(new_list)

print(America)

