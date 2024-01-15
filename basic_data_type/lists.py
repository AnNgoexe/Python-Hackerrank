# match - case method
if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(0, N):
        row = input().split()
        command = row[0]
        match command:
            case 'insert':
                lst.insert(int(row[1]), int(row[2]))
            case 'print':
                print(lst)
            case 'remove':
                lst.remove(int(row[1]))
            case 'append':
                lst.append(int(row[1]))
            case 'sort':
                lst.sort()
            case 'pop':
                lst.pop()
            case _:
                lst.reverse()

# If - else method
if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(0, N):
        row = input().split()
        if row[0] == 'insert':
            lst.insert(int(row[1]), int(row[2]))
        elif row[0] == 'print':
            print(lst)
        elif row[0] == 'remove':
            lst.remove(int(row[1]))
        elif row[0] == 'append':
            lst.append(int(row[1]))
        elif row[0] == 'sort':
            lst.sort()
        elif row[0] == 'pop':
            lst.pop()
        else:
            lst.reverse()
