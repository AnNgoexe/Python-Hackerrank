from itertools import groupby

string = input()
list1 = []
for (key, group) in groupby(string):
    list1.append((len(list(group)), int(key)))
print(*list1)