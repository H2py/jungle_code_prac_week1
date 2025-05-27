import sys
import heapq
input = sys.stdin.readline

n = int(input())

pq = []
for _ in range(n):
    cmd = int(input())
    
    if cmd == 0 and pq:
        sys.stdout.write(str(heapq.heappop(pq) * -1) + '\n')
    elif cmd == 0 and not pq:
        sys.stdout.write(str(0) + '\n')
    else:
        heapq.heappush(pq, cmd * (-1))
