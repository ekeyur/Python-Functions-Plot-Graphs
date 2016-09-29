from turtle import *
import shapes
import math
from random import randint

speed(0)
bgcolor("black")
home()
for i in range(1,1001):
    up()
    if i % 10 == 0:
        home()
    size = randint(5,15)
    x = randint(-600,600)
    y = randint(-600,600)
    setheading(randint(0,300))
    if (i%2 == 0):
        forward(x)
    else:
        forward(y)
    down()
    shapes.star(size,"grey",True)
mainloop()
