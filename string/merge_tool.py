def merge_the_tools(st, size):
    length = len(st)
    for i in range(0, length - size + 1, size):
        substring = st[i:i + size]
        print(''.join(dict.fromkeys(substring)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
