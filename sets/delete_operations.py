number_elements = int(input())
elements = set(map(int, input().split()))

number_operations = int(input())
for _ in range(number_operations):
    cmd = list(input().split())
    if len(cmd) == 1:
        elements.pop()
    else:
        value = int(cmd[1])
        operation = cmd[0]
        if operation == "discard":
            elements.discard(value)
        else:
            elements.remove(value)
print(sum(elements))