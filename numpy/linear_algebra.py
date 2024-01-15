import numpy

size = int(input())
row = []
for _ in range(size):
    row.append(list(map(float, input().split())))
print(round(float(numpy.linalg.det(row)), 2))


"""
------- Method 2
import numpy as np

size = int(input())
row = [list(map(float, input().split())) for _ in range(size)]
print(round(float(np.linalg.det(row)), 2))
"""