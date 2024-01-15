a, b = int(input()), int(input())
res = tuple(divmod(a, b))
print(a // b, a % b, res, sep="\n")