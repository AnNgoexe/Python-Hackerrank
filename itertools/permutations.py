from itertools import permutations

word, length = input().split()

for perm in permutations(sorted(word), int(length)):
    print("".join(perm))