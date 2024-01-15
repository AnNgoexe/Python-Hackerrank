import numpy

arr = list(map(int, input().split()))
print(numpy.reshape(arr, (3, 3)))

"""
----- Method 2
a = numpy.array(arr)
a = a.reshape((3, 3))
print(a)
"""