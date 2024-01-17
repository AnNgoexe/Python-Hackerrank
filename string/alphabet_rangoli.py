import string


def print_rangoli(size):
    alphabets = string.ascii_lowercase[:size]
    for i in range(size - 1, -size, -1):
        st = alphabets[size - 1: abs(i): -1] + alphabets[abs(i):]
        print("-".join(st).center(size * 4 - 3, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
