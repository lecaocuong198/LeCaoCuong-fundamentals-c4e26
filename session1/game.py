from turtle import *
m = 10

shape("turtle")
speed(6)

for i in range(30):
    for n in range(2):
        forward(m)
        left(90)

    m+=10
    forward(m)
    

mainloop()