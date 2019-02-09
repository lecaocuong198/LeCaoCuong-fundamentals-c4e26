items = ["T-Shirt","Sweater"]

print("Welcome to our shop!\nWhat do u want? (C, R, U, D): ")
a = input()

if(a == "C"):
    n = input("Enter new item: ")
    items.append(n)
    print(",".join(items))

if (a == "R"):
    print(",".join(items))

if (a=="U"):
    print(" ".join(items))
    n = int(input("Update Position? "))
    c = input("What's the new content? ")
    items[n] = c
    print("New list: ",items)

if (a=="D"):
    print(" ".join(items))
    n =  int(input("Enter the position u wanna remove: "))
    items.remove(items[n])
    print("The new list is :"," ".join(items))