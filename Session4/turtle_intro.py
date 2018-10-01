from turtle import *

shape("turtle")
color ("blue")
speed(0)

for i in range (300):
    for i in range (4):
        forward(200)
        left(180 - 60)
    
    left(7)

mainloop()