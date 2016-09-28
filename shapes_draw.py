from turtle import *
import shapes
import math
from random import randint


#coord_list = [(-150,-100),(50,50),(-50,150),(-150,150),(100,-100),(-200,-200)]
coord_list = [(50,-200,50, True),(100,100,50, True),(-250,100,50, False),(150,130,25,False),(250,-100,60,True),(-300,-200, 1, False)]
color_list = ['orange', 'blue', 'red', 'green', 'grey', 'purple' ]

shapes_list = [shapes.eq_tri,shapes.square,shapes.hexagon,shapes.star,shapes.octagon,shapes.circle]

for i in range(len(shapes_list)):
    up()
    #home()
    setheading(100)
    y,x,z,bul = coord_list[i]
    forward(x)
    setheading(0)
    forward(y)
    down()
    color(color_list[i],color_list[len(shapes_list)-1-i])
    if bul:
        begin_fill()

        end_fill()
    else:
        shapes_list[i](z)

mainloop()
