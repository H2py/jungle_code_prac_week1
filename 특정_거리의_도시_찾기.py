from collections import deque
import sys
input = sys.stdin.readline

N,M,K,X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, start, target):
    visited = [False] * (N+1)
    visited[start] = True
    queue = deque([(start, 0)])
    result = []
    
    while queue:
        node, cur_dist = queue.popleft()
        
        if cur_dist == target:
            result.append(node)
            continue
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, cur_dist+1))
                
    return result
        
                
result = bfs(graph, X, K)

if not result:
    print(-1)
else:
    for city in sorted(result):
        print(city)