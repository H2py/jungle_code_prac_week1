import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M, S = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
order = [0] * (N + 1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def dfs(v):
    global cnt
    visited[v] = True
    cnt += 1
    order[v] = cnt
    for neighbor in sorted(graph[v]):
        if not visited[neighbor]:
            dfs(neighbor)

dfs(S)
for i in range(1, N+1):
    print(order[i])