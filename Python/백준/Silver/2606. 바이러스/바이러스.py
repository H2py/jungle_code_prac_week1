import sys
input = sys.stdin.readline
cmp = int(input())
n = int(input())

cnt = 0
visited = [False] * (cmp+1)
graph = [[] for _ in range(cmp+1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v):
    global cnt
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            cnt +=1
        
dfs(1)
print(cnt)