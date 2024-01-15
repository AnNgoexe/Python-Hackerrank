from collections import Counter

number_words = int(input())
word_list = [input() for _ in range(number_words)]
counter = Counter(word_list)

print(len(counter))
print(*counter.values())
