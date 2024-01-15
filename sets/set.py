# Method 1
def average(array):
    distinct_heights = set(array)
    avg_heights = sum(distinct_heights) / len(distinct_heights)
    return round(avg_heights, 3)    # return f"{avg_heights:.3f}"

"""
# Method 2
import statistics


def average(array):
    def average(array):
    distinct_heights = set(array)
    avg_heights = statistics.mean(distinct_heights)
    return round(avg_heights, 3)    # return f"{avg_heights:.3f}"
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)