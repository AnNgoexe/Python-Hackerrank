if __name__ == '__main__':
    information_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        information_list.append([name, score])
    second_minimum_score = sorted(set(score_list))[1]
    sorted_name_list = sorted(list(name for name, score in information_list if score == second_minimum_score))
    print("\n".join(sorted_name_list))


