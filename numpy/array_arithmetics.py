import numpy as np
n, m = map(int, input().split())
first = np.array([input().split() for _ in range(n)], dtype='int')
second = np.array([input().split() for _ in range(n)], dtype='int')

print(first + second)  # np.add(first, second) cũng cho kết quả tương tự

print(first - second)  # np.subtract(first, second) cũng cho kết quả tương tự

print(first * second)  # np.multiply(first, second) cũng cho kết quả tương tự

print(first // second)  # np.floor_divide(first, second) cũng cho kết quả tương tự

print(first % second)  # np.mod(first, second) cũng cho kết quả tương tự

print(first ** second)  # np.power(first, second) cũng cho kết quả tương tự