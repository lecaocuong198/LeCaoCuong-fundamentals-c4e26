import random

words = ["random","total","director","world"]
n = random.choice(words)
l = len(n)
chuoi = []

for i in range(l):
    chuoi.append(n[i:i+1])

for i in range(l):
    j = random.choice(chuoi)
    print(j,end=" ")
    chuoi.remove(j)
check = 1

while (check ==1):
    result = input("\nWhat's your answer?\n")
    if (result == n ):
        check = 0
        print("Correct!")
    else:
        print("Wrong! Wanna try again? ")
        p =  input("1: Try agian \n2: No,I quit! ")
        if(p==1):
            print("Fighting!")
        else:
            print("Game Over!")
            check = 0
