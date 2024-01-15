if __name__ == '__main__':
    number = int(input().strip())
    if number % 2 != 0:
        print("Weird")
    if (number >= 2) and (number <= 5) and number % 2 == 0 and number % 4 == 0:
        print("Not Weird")
    if (number >= 6) and (number <= 20) and number % 2 == 0:
        print("Weird")
    if (number > 20) and number % 2 == 0:
        print("Not Weird")
