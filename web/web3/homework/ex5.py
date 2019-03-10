from ex4 import river_collection



if __name__=="__main__":

    Africa= []
    Africa_list = river_collection.find(
        {
            "continent": {"$eq": "Africa",}
        }
    )
    for country in Africa_list:
        new_list = {
            "name" : country["name"],
            "continent": country["continent"],
            "length": country["length"]
        }
        Africa.append(new_list)


    print(Africa)
