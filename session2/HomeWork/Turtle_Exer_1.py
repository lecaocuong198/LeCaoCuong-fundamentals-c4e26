from turtle import *

shape("turtle")
speed(8)

color('red','red')
begin_fill()
for i in range(4):
    right(30)
    forward(60)
    left(60)
    forward(60)
    left(120)
    forward(60)
    left(60)
    forward(60)
    right(120)
    
end_fill()

mainloop()