Colors_list = ['red', 'green', 'blue','teal','gray', 'black']

n = len(Colors_list)
m = 360/n
from turtle import *

shape("turtle")
width(5)


for i in range (n):
    forward(80)
    left(m)
    forward(80)
    color(Colors_list[i])
    

mainloop()