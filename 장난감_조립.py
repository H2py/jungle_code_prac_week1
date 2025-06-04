import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    mid, base, num = map(int ,input().split())
    graph[mid].append((base, num))
    
def topological_sort(graph, n):
    in_degree = [0] *(n+1)
    
    for node in range(1, n+1):
        for neighbor in graph[node]:
            in_degree[neighbor] +=1
            
    queue = deque([i for i in range(1, n+1) if in_degree[i] == 0])
    result = 0
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0 :
                queue.append(neighbor)
                
    if len(result) != n:
        return None
    
    return result