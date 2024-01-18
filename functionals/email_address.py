import re


def fun(s):
    pattern = r'[a-zA-Z0-9\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    if re.fullmatch(pattern, s):
        return True
    else:
        return False


def filter_mail(email_list):
    return list(filter(fun, email_list))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
