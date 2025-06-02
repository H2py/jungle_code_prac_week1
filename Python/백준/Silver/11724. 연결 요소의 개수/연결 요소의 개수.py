import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

cnt = 0
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
            
for i in range(1, N+1):
    if not visited[i]:
        cnt +=1
        dfs(i)
            
print(cnt)