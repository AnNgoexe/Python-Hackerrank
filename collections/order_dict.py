from collections import OrderedDict

num_items = int(input())
items = OrderedDict()

for _ in range(num_items):
    item, space, quantity = input().rpartition()
    quantity = int(quantity)
    if item in items:
        items[item] += quantity
    else:
        items[item] = quantity

for item, net_price in items.items():
    print(item, net_price)

"""
import collections

d = collections.OrderedDict()
for _ in range(int(input())):
    item = input().rsplit(" ", 1)
    if item[0] in d.keys():
        d[item[0]] = d[item[0]] + int(item[1])
    else:
        d[item[0]] = int(item[1])
        
for key, item in d.items():
    print(key, item)
"""