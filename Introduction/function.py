def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


input_year = int(input())
print(is_leap(input_year))
