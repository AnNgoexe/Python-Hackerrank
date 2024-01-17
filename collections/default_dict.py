from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(n):
    w = input()
    d[w].append(str(i + 1))

for _ in range(m):
    w = input()
    print(" ".join(d[w]) if len(d[w]) != 0 else -1)