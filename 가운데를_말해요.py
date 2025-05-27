import heapq
import sys

input = sys.stdin.readline
n = int(input())

left = []  
right = [] 

for _ in range(n):
    num = int(input())

    heapq.heappush(left, -num)

    if right and -left[0] > right[0]:
        max_left = -heapq.heappop(left)
        heapq.heappush(right, max_left)

    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))

    sys.stdout.write(str(-left[0]) + '\n')
