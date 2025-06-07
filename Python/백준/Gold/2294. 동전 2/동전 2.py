import sys
from collections import deque
input = sys.stdin.readline

n,target = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
visited = set()
visited.add(0)
    
# 현재 코인, cnt
q = deque([(0,0)])

while q:
    cur_v, cnt = q.popleft()
    
    if cur_v == target:
        print(cnt)
        sys.exit()
    
    for coin in coins:
        next_v = cur_v + coin
        if not next_v in visited and next_v <= target :
            visited.add(next_v)
            q.append((next_v, cnt+1))
        
print(-1)