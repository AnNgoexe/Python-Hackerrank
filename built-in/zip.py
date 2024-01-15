n, x = map(int, input().split())
a = [list(map(float, input().split())) for i in range(x)]
b = zip(*a)
for i in b:
    print(sum(i)/len(i))