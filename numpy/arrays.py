import numpy


def arrays(arr):
    my_arr = numpy.array(arr, float)
    return numpy.flip(my_arr)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
