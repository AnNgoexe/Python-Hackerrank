import re


s = input()

res = re.findall(f'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', s)
if res:
    for i in res:
        print(i)
else:
    print(-1)