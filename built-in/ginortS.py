string = input()
lowercase_list = [i for i in string if i.islower()]
supercase_list = [i for i in string if i.isupper()]
odd_digits_list = [i for i in string if i.isdigit() and int(i) % 2 != 0]
even_digits_list = [i for i in string if i.isdigit() and int(i) % 2 == 0]

print(''.join(sorted(lowercase_list) + sorted(supercase_list) + sorted(odd_digits_list) + sorted(even_digits_list)))
