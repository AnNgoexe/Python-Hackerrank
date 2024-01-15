import numpy

n = list(map(int, input().split()))
A = numpy.array(n, dtype=int)
m = list(map(int, input().split()))
B = numpy.array(m, dtype=int)
print(numpy.inner(A, B))
print(numpy.outer(A, B))
