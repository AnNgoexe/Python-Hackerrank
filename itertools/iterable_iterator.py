from itertools import combinations


_ = int(input())
chars = input().split()
k = int(input())

combin = list(combinations(chars, k))
contain_a = [tup for tup in combin if 'a' in tup]
print(len(contain_a) / len(combin))