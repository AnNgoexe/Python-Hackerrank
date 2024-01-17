from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input().split())
data = [Student(*list(map(str, input().split()))) for line in range(n)]

print(sum([int(i.MARKS) for i in data])/n)