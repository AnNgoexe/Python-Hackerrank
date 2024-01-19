import re

string = input()
pattern = r"([A-Za-z0-9])\1"
match = re.search(pattern, string)
print(match.group(1) if match else -1)