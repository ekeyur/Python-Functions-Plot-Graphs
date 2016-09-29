import matplotlib.pyplot as plot


def far(x):
    return (x * 9/5) + 32

xs = range(-150,151)
ys = []
for x in xs:
    ys.append(far(x))

plot.plot(xs,ys)
plot.show()
