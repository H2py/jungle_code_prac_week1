import sys
import heapq

input = sys.stdin.readline
n = int(input())
homes = [sorted(map(int, input().split())) for _ in range(n)]
homes.sort(key=lambda x: x[1])

d = int(input())
heap = []
result = 0
for start, end in homes:
    if end - start > d:
        continue
    
    heapq.heappush(heap, start)
    
    while heap and heap[0] < end - d:
        heapq.heappop(heap)
    
    result = max(result, len(heap))

print(result)