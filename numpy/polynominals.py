import numpy

poly = list(map(float, input().split()))

val = int(input())

print(numpy.polyval(poly), val)
