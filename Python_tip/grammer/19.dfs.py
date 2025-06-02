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



def dfs_iterative(v):
    stack = [v]
    visited = [0] * (N+1)
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            print(node, end=' ')
            for i in range(N, 0, -1):
                if graph[node][i] == 1 and not visited[i]:
                    stack.append(i)