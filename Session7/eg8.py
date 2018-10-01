n = int(input("Input the number of side you want!"))
m = 360/n
from turtle import *

shape("turtle")
color ("blue")



for i in range (n):
    forward(100)
    left(m)
    forward(100)
    

mainloop()