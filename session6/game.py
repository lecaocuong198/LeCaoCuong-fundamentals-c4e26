from random import randint, choice
import calc
# from calc import evaluate
score = 0
while True:
    a = randint(0,9)
    b = randint(0,9)
    pt = choice(['+','-','*','/'])
    s = calc.evaluate(a,b,pt)
    c = s + randint(-1,1)
    abc = f"{a} {pt} {b} = {c}"
    print(abc)
    check = input("(Y)es/(N)o/(E)xit?")
    if check == "e" or check == "E":
        break
    print("******************")

    if s == c and check == ("y"):
        score += 1
        print("Yay!   Score =",score)
    if s == c and check == ("n"):
        score = 0
        print("Wrong!   Score =",score)      
    if s != c and check == ("n"):
        score += 1
        print("Yay!   Score =",score)      
    if s !=c and check == ("y"):
        score = 0 
        print("Wrong!   Score =",score)
    print("******************")

#string formating
# s = f"{x} + {y} = {c}"
# print(s)
