import sys
import heapq

input = sys.stdin.readline
n = int(input())
h = list(map(int, sys.stdin.readlines()))
heapq.heapify(h)
total = 0
for _ in range(n-1):
    n1, n2 = heapq.heappop(h), heapq.heappop(h)
    heapq.heappush(h, n1+n2)
    total += n1 + n2
    
print(total)