if __name__ == '__main__':
    s = input()
    lst = ['False', 'False', 'False', 'False', 'False']
    for elem in s:
        if elem.isalnum():
            lst[0] = 'True'
        if elem.isalpha():
            lst[1] = 'True'
        if elem.isnumeric():
            lst[2] = 'True'
        if elem.islower():
            lst[3] = 'True'
        if elem.isupper():
            lst[4] = 'True'
    lst = '\n'.join(lst)
    print(lst)

"""
------- Method 2
import re

if __name__ == '__main__':
    s = input()

    print(re.search('[a-zA-Z0-9]', s) != None)
    print(re.search('[a-zA-Z]', s) != None)
    print(re.search('[0-9]', s) != None)
    print(re.search('[a-z]', s) != None)
    print(re.search('[A-Z]', s) != None)
    
    
------- Method 3
if __name__ == '__main__':
    s = input()
    
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.isupper() for i in s))
    print(any(i.islower() for i in s))
    

-------- Method 4
if __name__ == '__main__':
    s = input()
    attrs = ["isalnum", "isalpha", "isdigit", "islower", "isupper"]
    for attr in attrs:
        print(any(getattr(i, attr)() for i in s))
"""
