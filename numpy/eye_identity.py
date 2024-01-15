import numpy

numpy.set_printoptions(legacy = "1.13")
rows, cols = map(int, input().split())
matrix = numpy.eye(rows, cols, k = 0)
print(matrix)
