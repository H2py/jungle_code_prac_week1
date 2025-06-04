INF = float('inf')

def floyd_warshall(graph, V):
    dist = [[INF] * V for _ in range(V)]
    
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
            
    for i in range(V):
        dist[i][i] = 0
        
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
    return dist

V = 4
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

result = floyd_warshall(graph, V)