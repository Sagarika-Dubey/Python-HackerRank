import numpy

P = numpy.array((input().split()), dtype='float')
x = int(input().strip())

print(numpy.polyval(P, x))