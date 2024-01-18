from itertools import product

k, m = map(int, input().split())
result = 0
lsts = []
for _ in range(k):
    lsts.append(list(map(int, input().split()))[1:])

for arr in product(*lsts):
    re = sum(x ** 2 for x in arr) % m
    result = max(result, re)

print(result)

