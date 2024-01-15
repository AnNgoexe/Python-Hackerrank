from collections import Counter

n, m = map(int, input().split())
array = list(map(int, input().split()))
array_counter = Counter(array)
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
happiness = 0
for i in (set_a.intersection(set(array))):
    happiness += array_counter[i]
for i in (set_b.intersection(set(array))):
    happiness -= array_counter[i]
print(happiness)


"""
--------- Method 2
a, b = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = set(map(int, input().split()))
array3 = set(map(int, input().split()))
happiness = 0
for x in array1:
    if x in array2:
        happiness +=1
    elif x in array3:
        happiness -=1
print(happiness)
"""