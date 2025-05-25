import sys
sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(100000)
def largest_rectangle(heights, start, end):
    if start > end:
        return 0

    min_index = start
    for i in range(start, end + 1):
        if heights[i] < heights[min_index]:
            min_index = i

    current_area = heights[min_index] * (end - start + 1)
    left_area = largest_rectangle(heights, start, min_index - 1)
    right_area = largest_rectangle(heights, min_index + 1, end)

    return max(current_area, left_area, right_area)

while True:
    inputs = list(map(int, sys.stdin.readline().split()))
    if inputs[0] == 0:
        break
    n = inputs[0]
    histogram = inputs[1:]
    print(largest_rectangle(histogram, 0, n - 1))
