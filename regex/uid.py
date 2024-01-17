import re


def has_ten_alpha_digit(s):
    return re.search(r'^[a-zA-Z0-9]{10}$', s)


def is_not_repeat(s):
    return len(s) == len(set(s))


def has_two_upper(s):
    return re.search(r'[A-Z].*[A-Z]', s)


def has_three_digits(s):
    return re.search(r'[0-9].*[0-9].*[0-9]', s)


n = int(input())
for _ in range(n):
    uid = input()
    if has_ten_alpha_digit(uid) and is_not_repeat(uid) and has_two_upper(uid) and has_three_digits(uid):
        print("Valid")
    else:
        print("Invalid")