ship = [5,7,300,90,24,50,75]
print("My ship sizes: ",ship)
print("Now my biggest sheep has size ",max(ship),"let's shear it")
n = ship.index(max(ship))
ship[n] = 8
print("After shearing, here is my flock: ",ship)
for j in range(3):
    for i in range(len(ship)):
        ship[i] +=50
    print("Month",j+1,"\nOne month has passed, here is my flock: ",ship)
    print("Now my biggest sheep has size ",max(ship),"let's shear it")
    n = ship.index(max(ship))
    ship[n] = 8
    print("After shearing, here is my flock: ",ship)
    s = 0
for i in range(len(ship)):
    s +=ship[i]
print("My flock has size in total: ",s)
print("I'd get",s,"*2$ =",s*2,"$")
