from turtle import *
speed(0)
colormode(255)
width(5)
for i in range (300):
    color(i*20,i*10,i*30)
    for i in range (4):
        forward(200)
        left(90)

    left(7)
mainloop()