import re


def checkRepeat(s):
    s = ''.join(i for i in s if i.isdigit())
    return re.search(r'([0-9])\1{3}', s)


def checkCard(s):
    return re.search(r'^[4-6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$', s)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        num = input()
        if not checkRepeat(num) and checkCard(num):
            print("Valid")
        else:
            print("Invalid")