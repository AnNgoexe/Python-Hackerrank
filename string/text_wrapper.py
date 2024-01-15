import textwrap


def wrap(st, width):
    text_wrap = textwrap.fill(st, width)
    return text_wrap


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
