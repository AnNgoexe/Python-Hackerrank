rows, cols = map(int, input().strip().split())
def generate_rows(times):
    st = ".|."
    return (st * times).center(cols, "-")

# top rows
for i in range(1, rows, 2):
    print(generate_rows(i))

# Center row
print("WELCOME".center(cols, "-"))

# bottom rows
for i in range(rows - 2, 0, -2):
    print(generate_rows(i))

"""
------- Method 2
rows, cols = map(int, input().strip().split())
st = ".|."
print("\n".join([(st * i).center(cols, "-") for i in list(range(1, rows, 2)) + ["WELCOME"] + list(range(rows - 2, 0, -2))]))
"""