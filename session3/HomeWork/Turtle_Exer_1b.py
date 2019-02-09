from turtle import*

shape("turtle")

colors = ['red','blue','brown','yellow','grey']
speed(8)

for i in range(5):
    color(colors[i],colors[i])
    begin_fill()
    for j in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()

mainloop()
