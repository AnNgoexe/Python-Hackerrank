import re
S, k = input(), input()
matches = re.finditer(f'(?=({k}))', S)
matches_list = list(matches)


if len(matches_list) > 0:
    for match in matches_list:
        print(tuple((match.start(), match.end() + len(k) - 1)))
else:
    print((-1, -1))