import re


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

z = list(zip(*matrix))
result = ""
for i in z:
    result += "".join(i)
pattern = r"\b[^a-zA-Z0-9]+\b"
print(re.sub(pattern, " ", result))