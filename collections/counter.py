from collections import Counter

n = int(input())
sizes = Counter(map(int, input().split(' ')))
m = int(input())
total = 0

for _ in range(m):
    size_desired, price = map(int, input().split(' '))
    if sizes[size_desired] > 0:
        total += price
        sizes[size_desired] -= 1
print(total)