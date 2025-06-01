def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)           

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}


visited = [False] * 6



def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
            
            
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True