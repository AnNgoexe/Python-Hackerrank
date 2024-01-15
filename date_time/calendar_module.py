import calendar

month, day, year = map(int, input().split())
wday = calendar.weekday(year, month, day)
print(calendar.day_name[wday].upper())

