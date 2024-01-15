def is_vowel(letter):
    return letter in 'AEIOU'


def minion_game(string):
    kevin_score, stuart_score = 0, 0
    length = len(string)
    for i in range(len(string)):
        if is_vowel(string[i]):
            kevin_score += (length - i)
        else:
            stuart_score += (length - i)
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
