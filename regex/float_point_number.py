import re

number_tests = int(input())
for _ in range(number_tests):
    val = input()
    print(bool(re.search(r"^[+-]?\d*\.\d+$", val) and float(val)))