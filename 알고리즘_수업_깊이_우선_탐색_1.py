N, M, S = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(N):
    u, v = map(int, input().split())
    graph[u].append(v)
    
def dfs(v):
    visited[v] = True
    print(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(v+1)

dfs(S)
print(0)