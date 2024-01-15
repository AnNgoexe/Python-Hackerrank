a, b = map(int, input().split())
expression = input()
print(b == eval(expression, a))