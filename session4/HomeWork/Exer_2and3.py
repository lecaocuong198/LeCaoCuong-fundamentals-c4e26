print("Answer the following algebra question:\nIf x = 8, then what is the value of 4(x+3)? ")
answer = {
    1: 35,
    2: 36,
    3: 40,
    4: 44,
}
for i in answer:
    print(i,". ",answer[i])
n = int(input())
x = 0

score = {
        1: "About 55",
        2: "About 64",
        3: "About 75",
        4: "About 85",
    }
if n==4 or n == 44:
    print("Bingo")
    x+=1
else:
    print("Wrong! Estimate this answer(exact calculation not needed): ")
    
print("Jack scored these marks in 5 math tests: 48, 81, 72, 66 and 52. What's the mean? ")
for i in score:
    print(i,".",score[i])
da = input()
if da == "2" or da =="About 64":
    print("Bingo")
    x+=1
else:
    print("Wrong!")
print("You correcly answer",x,"of 2 question")
