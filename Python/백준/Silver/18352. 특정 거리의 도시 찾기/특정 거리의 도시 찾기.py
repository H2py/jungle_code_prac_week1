from collections import deque
import sys
input = sys.stdin.readline

N,M,K,X = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)

result = []
def dfs(graph, start, target):
    global result
    visited[start] = True
    
    queue = deque([(start, 0)])
    
    while queue:
        node, cur_dist = queue.popleft()
        
        if cur_dist == target:
            result.append(node)
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, cur_dist+1))
        
                
dfs(graph, X, K)
if not result:
    print(-1)
else:
    result.sort()
    for v in result:
        print(v)