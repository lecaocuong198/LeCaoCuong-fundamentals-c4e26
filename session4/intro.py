# person = ["MR.D",24,"HaNoi",11,False,430,True]

# person = {}
# print(person)
# print(type(person))

# person = {
#     "name": "MR.D"#Key:Value
# }
# print(person)

# person = {
#     "name": "MR.D",
#     "age": 24,
#     "location": "HaiPhong",
#     "Status": False,

# }
# print(person["name"])

diction = {"name": "MR.D",
"age": 24,
"location": "HaiPhong",
"status": False,
"favs": ["books","movies","music"],
}
# x=1
# while(x==1):
#     print("")
#     print(*diction)
#     print("\nEnter 0 to end\n")
#     n =input("what's u wanna know?\n*********************************** \n")
#     if(n==0):
#         x=0
#     if n in diction:
#         print(diction[n])
#         print("********************************")
#     else:
#         print("Not found!")

#CREATE
# diction["friend_cout"] = 450
# print(diction["friend_cout"])
#vong for chay theo value for v in diction.values():

fs = diction["favs"]

# loop = 1
# while loop ==1:    
    # print(*diction)
    # print("What you wanna do?\nCreate   Read   Update   Delete   Exit\n")
    # work = input("\nEnter the key ")

    # if work == "Read":
    # #Read
    #     n = input("What u wanna know?")
    #     if n in diction:
    #         print(diction[n])
    #         print("********************************")
    #         print("Wanna continue? (Y/N) ")
    #         check =  input("")
    #         if check == "N":
    #             loop = 0
    #     else:
    #         print("not found, do u want contribute this word? (Y/N)").upper()
    #         check = input("")
    #         if check == "Y":
    #             i= input("Enter the translation: ")
    #             diction[n] = i
    #             print("New diction: ",end = " ")
    # #Update
    # if work == "Update":
    #     n = input("What key u wanna update?\n")
    #     if n in diction:
    #         content = input("what's the new content? ")
    #         diction[n] = content
    #         print("New diction:",end = " ")
    #     else:
    #         print("not found, do u want contribute this word? (Y/N)").upper()
    #         check = input("")
    #         if check == "Y":
    #             i= input("Enter the translation: ")
    #             diction[n] = i
    #             print("New diction:",end = " ")
    # #Update
    # if work == "Delete":
    #     n = input("What key u wanna del? ")
    #     if n in diction:
    #         del diction[n]
    #         print("New diction: ",end = "")
    #     else:
    #         i = input("Key not found! Wanna continue? (Y/N) ").upper()
    #         if i == "N":
    #             loop = 0
    # #Exit
    # if work == "Exit":
    #     loop =0
    # #Create
    # if work == "Create":
    #     n = input("Enter key name? ")
    #     i= input("Enter the translation: ")
    #     diction[n] = i
    #     print("New diction: ",end =" ")

p0 = {"name": "MR.D",
"age": 24,
"location": "HaiPhong",
"status": False,
"favs": ["books","movies","music"]
}

p1 = {
    "name": "Hoang",
    "age":21,
    "location": "Hanoi",
    "status": "...",
}

p2 = {
    "name":"Son",
    "age":18,
    "location": "Hanoi",
    "status": "...",
}

p_list = [{"name": "MR.D",
"age": 24,
"location": "HaiPhong",
"status": False,
"favs": ["books","movies","music"]
},{
    "name": "Hoang",
    "age":21,
    "location": "Hanoi",
    "status": "...",
},{
    "name":"Son",
    "age":18,
    "location": "Hanoi",
    "status": "...",
}]

j = 0
# for i in p_list:
#     print(i["name"])
print(p_list[0]["location"])
#json
