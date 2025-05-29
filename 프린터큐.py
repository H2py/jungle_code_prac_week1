import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    q = deque((i, p) for i, p in enumerate(priorities))
    
    count = 0
    while q:
        cur = q.popleft()
        if (cur[1] < other[1] for other in q):
            q.append(cur)
        else:
            count +=1
            if cur[0] == m:
                print(count)
                break     