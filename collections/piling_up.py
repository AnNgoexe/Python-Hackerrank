from collections import deque


def is_stackable(cubes):
    cubes = deque(cubes)
    last = float('inf')

    while cubes:
        left, right = cubes[0], cubes[-1]
        if last >= right >= left:
            last = cubes.pop()
        elif last >= left >= right:
            last = cubes.popleft()
        else:
            return "No"

    return "Yes"


number_queries = int(input())
for _ in range(number_queries):
    _ = int(input())
    blocks = list(map(int, input().split()))
    print(is_stackable(blocks))