import matplotlib.pyplot as pyplot

# pyplot.plot([1,2,3,4])
# pyplot.show()

x = range(10000)
y = [v*v for v in x]
pyplot.plot(x, y, 'bs')
pyplot.show()