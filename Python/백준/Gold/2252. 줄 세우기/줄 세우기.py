import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    
def topological_sort(graph, n):
    in_degree = [0] * (n + 1)
    
    for node in range(1, n+1):
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
            
    queue = deque([i for i in range(1, n+1) if in_degree[i] == 0])        
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    if len(result) != n:
        return None
    
    return result

result = topological_sort(graph, N)

print(*result)