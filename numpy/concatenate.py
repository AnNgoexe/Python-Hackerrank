import numpy
n, m, p = map(int, input().split())
first_matrix = numpy.array([list(map(int, input().split())) for _ in range(n)])
second_matrix = numpy.array([list(map(int, input().split())) for _ in range(m)])
print(numpy.concatenate((first_matrix, second_matrix), axis=0))