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
}

visited = [False] * 6


from collections import deque

def bfs(graph, start):
    visited = [False] * (len(graph) + 1)
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor) 