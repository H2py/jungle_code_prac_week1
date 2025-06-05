import sys
from collections import deque
input = sys.stdin.readline

start, target = map(int, input().split())
visited = [False] * (max(start, target) * 2 + 1)

def bfs(start):
    visited[start] = True
    q = deque([(start, 0)])
    
    while q :
        v, cnt = q.popleft()
        
        if v == target:
            return cnt
        for next in [v-1, v+1, v*2]:
            if 0 <= next < len(visited) and not visited[next]:
                visited[next] = True
                q.append((next, cnt+1))         
print(bfs(start))            