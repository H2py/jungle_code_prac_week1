import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
order = [0] * (N+1)
cnt = 0

for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for edges in graph:
    edges.sort(reverse=True)

def bfs(start):
    global cnt
    visited[start] = True
    q = deque([start])
    
    while q:
        v = q.popleft()
        cnt += 1
        order[v] = cnt
        
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                
                
bfs(R)
for i in range(1, N+1):
    print(order[i])