import numpy

row, col = map(int, input().split())
arr = numpy.array([list(input().split()) for _ in range(row)], dtype='int')
print(numpy.max(numpy.min(arr, axis=1), axis=0))
