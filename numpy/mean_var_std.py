from numpy import mean, std, var, array

row, _ = map(int, input().split())
A = array([input().split() for _ in range(row)], dtype='int')
print(mean(A, axis = 1), var(A, axis = 0), round(std(A, axis = None), 11), sep = '\n')
