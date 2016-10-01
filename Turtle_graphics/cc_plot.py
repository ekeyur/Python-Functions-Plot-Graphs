import matplotlib.pyplot as plot
import math

def y1(x):
    return x+10

def y2(x):
    return x-10

def y3(x):
    return 100

xs = range(0,101)
yy = []
yg = []
yr = []

for x in xs:
    yy.append(y1(x))
    yg.append(y2(x))
    yr.append(y3(x))

plot.xlim(0,100)
plot.ylim(0,100)

plot.plot(xs,yr,xs,yy,xs,yg)

plot.fill_between(xs,yr, color='red')
plot.fill_between(xs,yy, color='yellow')
plot.fill_between(xs,yg, color='green')



plot.show()
