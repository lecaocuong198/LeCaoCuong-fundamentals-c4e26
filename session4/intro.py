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
"location": "HaiPhong",}
x=1
while(x==1):
    print("")
    print(*diction)
    print("\nEnter 0 to end\n")
    n =input("what's u wanna know?\n*********************************** \n")
    if(n==0):
        x=0
    if n in diction:
        print(diction[n])
        print("********************************")
    else:
        print("Not found!")



