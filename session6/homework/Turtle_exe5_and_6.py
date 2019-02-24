from turtle import *

def draw_Star(x,y,leght):
    penup()
    setx(x)
    sety(y)
    pendown()
    for i in range(10):
        forward(leght)
        left(144)
    mainloop()

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(30, 100)
    draw_Star(x, y, length)

