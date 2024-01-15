first_size = int(input())
first_set = set(map(int, input().split()))

second_size = int(input())
second_set = set(map(int, input().split()))

# Method1

sym_diff = first_set.symmetric_difference(second_set)  # sym_diff = first_set ^ second_set
for elem in sorted(sym_diff):
    print(elem)

"""
# Method 2
set_a_diff = set_a.difference(set_b)
set_b_diff = set_b.difference(set_a)
for i in sorted(set_a_diff.union(set_b_diff)):
    print(i)
"""
