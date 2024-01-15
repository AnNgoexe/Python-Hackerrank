import numpy

n = int(input())
A = numpy.array([input().split() for _ in range(n)], dtype = int)
B = numpy.array([input().split() for _ in range(n)], dtype = int)

print(numpy.dot(A, B))