N, M = map(int, input().split())
visited = [False] * (N+1)

graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N+1):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    
    for i in range(1, N+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)
    