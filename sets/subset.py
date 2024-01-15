query_number = int(input())
for _ in range(query_number):
    first_set_size = int(input())
    first_set = set(map(int, input().split()))

    second_set_size = int(input())
    second_set = set(map(int, input().split()))
    print(first_set.issubset(second_set))  # first_set <= second_set
