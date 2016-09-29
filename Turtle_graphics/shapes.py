from turtle import *

def eq_tri(size,col, fill):
    color(col)
    if fill:
        begin_fill()
        for i in range(3):
            forward(size)
            left(120)
        end_fill()
    else:
        for i in range(3):
            forward(size)
            left(120)

def square(size,col, fill):
    color(col)

    if fill:
        begin_fill()
        for i in range(4):
            forward(size)
            left(90)
        end_fill()
    else:
        for i in range(4):
            forward(x)
            left(90)

def hexagon(size,col, fill):
    color(col)
    left(30)

    if fill:
        begin_fill()
        for i in range(6):
            forward(size)
            left(60)
        end_fill()
    else:
        for i in range(6):
            forward(size)
            left(60)

def octagon(size,col, fill):
    color(col)
    left(30)

    if fill:
        begin_fill()
        for i in range(8):
            forward(size)
            left(45)
        end_fill()
    else:
        for i in range(8):
            forward(size)
            left(45)

def star(size,col, fill):
    color(col)

    if fill:
        begin_fill()
        for i in range(5):
            forward(size)
            left(144)
        end_fill()
    else:
        for i in range(5):
            forward(size)
            left(144)

def circle(size,col, fill):
    color(col)
    if fill:
        begin_fill()
        for i in range(360):
            forward(size)
            left(1)
        end_fill()
    else:
        for i in range(360):
            forward(size)
            left(1)



if __name__ == '__main__':
    mainloop()
