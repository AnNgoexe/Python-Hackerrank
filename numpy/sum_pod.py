import numpy as np
n, m = map(int, input().split())
A = np.array([input().split() for _ in range(n)], dtype='int')
print(np.prod(np.sum(A, axis=0), axis=None))