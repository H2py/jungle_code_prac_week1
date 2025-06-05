import sys
sys.setrecursionlimit(10**6)
N, M, S = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def dfs(v):
    visited[v] = True
    print(v)
    for neighbor in sorted(graph[v]):
        if not visited[neighbor]:
            dfs(neighbor)

dfs(S)
print(0)