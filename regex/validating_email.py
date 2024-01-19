import re

n = int(input())
pattern = r'^[a-zA-Z]([a-zA-Z0-9\_\.\-]+)@([a-zA-Z]+)\.([a-zA-Z]{1,3})$'
for _ in range(n):
    name, email = input().split()
    if re.match(pattern, email[1:-1]):
        print(name, email)
