import math

ab = int(input())
bc = int(input())

ac = math.sqrt(ab ** 2 + bc ** 2)
angle = round(math.asin(ab/ac)*180/math.pi)

print(f"{int(angle)}\u00b0")