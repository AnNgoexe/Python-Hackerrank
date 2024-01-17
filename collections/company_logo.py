from collections import Counter

if __name__ == '__main__':
    s = sorted(input())
    for item in Counter(s).most_common(3):
        print(*item)


"""
------ Method 2:
if __name__ == '__main__':
    s = sorted(input())
    char_count = Counter(s)
    sorted_char_count = sorted(char_count.items(), reverse = True, key = x : x[1]) 
    
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")
"""