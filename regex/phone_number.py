import re


condition = r"^[7-9]\d{9}$"
n = int(input())
for _ in range(n):
    phone_number = input()
    m = re.match(condition, phone_number)
    if m:
        print("YES")
    else:
        print("NO")