items = ["a","b","c","d"]

# print(items)
# n = int(input("Enter the position u wanna remove? "))
# items.pop(n)
# print(items)
# s = input("Enter the content u wanna delete? ")
# items.remove(s)
# print(items)

print(items)
q = input("What u wanna remove? ")
if (q.isnumeric()):
    s = int(q)
    items.pop(s)
    print(items)
else:
    items.remove(q)
    print(items)



# delete
# print(items)

# items.pop(1)

# print(items)

# items.remove("c")

# print(items)
# print(items)
# for i in range(len(items)):
#     print(items[i])

#for each
# no = 1
# for nb in items:
#     print(no,nb,sep = ".")
#     no +=1

# for i,food in enumerate(items,3):
#     print(i,food,sep = ". ")

# for i in range(len(items)):
#      print(items[i].upper(),end=" ")
# print("")
# for i,nb in enumerate(items,1):
#     print(i,nb)
# for i,nb in enumerate(items):
#     if (i<3):
#         Roman = "I"
#         for j in range(i):
#             Roman += "I"
#     if (i == 3):
#         Roman = "IV"

#     print(Roman,nb)

# pre = ["I","II","III","IV"]
# for p, f in zip(pre, items):
#     print(p,f)

# x =1
# while(x==1):
#     for i,nb in enumerate(items,1):
#         print(i,nb)
#     print("Enter 10000 to end the program!")
#     n =  int(input("Positin u wanna update? "))
#     if (n ==10000):
#         x = 0
#     if(n >len(items)):
#         print("Your input number is out of range!")
#     else:
#         w = input("What's the new content ")
#         if(n == 0 ):
#             items = w
#         else:
#             items[n-1] = w

