from collections import deque

times = int(input())
operations = [input().split() for _ in range(times)]

dq = deque()
for op in operations:
    if len(op) == 1:
        eval(f"dq.{op[0]}()")
    else:
        eval("dq.{}({})".format(op[0], int(op[1])))
print(*dq)