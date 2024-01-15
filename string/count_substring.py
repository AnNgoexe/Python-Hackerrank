def count_substring(st, sub_string):
    count = 0
    substring_length = len(sub_string)
    for i in range(len(st) - substring_length + 1):
        if st[i:i + substring_length] == sub_string:
            count += 1
    return count


if __name__ == "__main__":
    string = input().strip()
    substr = input().strip()
    cnt = count_substring(string, substr)
    print(cnt)
