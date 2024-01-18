def wrapper(function):
    def fun(li):
        function(["+91 " + num[-10:-5] + " " + num[-5:] for num in li])

    return fun


@wrapper
def sort_phone(phone_list):
    print(*sorted(phone_list), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

"""
-------- Method 2
def wrapper(function):
    def fun(li):
        function(["+91 " + num[-10:-5] + " " + num[-5:] for num in li])
    return fun

def sort_phone(phone_list):
    print(*sorted(phone_list), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    s = wrapper(sort_phone)
    s(l)
"""