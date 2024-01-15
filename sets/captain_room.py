k = int(input())
room_number_list = list(map(int, input().split()))
room_number_set = set(room_number_list)
room_number_list_sum = sum(room_number_list)
room_number_set_sum = sum(room_number_set) * k
diff = room_number_set_sum - room_number_list_sum
print(diff // (k-1))

"""
-------- Method 2
from collections import Counter

k = int(input())
room_number_list = list(map(int, input().split()))
room_number_counter = Counter(room_number_list)

single_occurrence_number = next(number for number, count in room_number_counter.items() if count == 1)
print(single_occurrence_number)
"""