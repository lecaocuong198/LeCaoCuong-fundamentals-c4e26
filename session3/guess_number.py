import random

x = random.randint(1,100)
loop = 0

while (loop<7):
    n = int(input("Doan di "))
    if (x>n):
        print("SO LON HON")
    elif (x<n):
        print("SO NHO HON")
    else:
        print("CORRECT!")
        loop = 8
    loop+=1
    if (loop == 7 ):
        print("Game Over!")