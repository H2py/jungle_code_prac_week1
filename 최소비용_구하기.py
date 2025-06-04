import heapq, sys
input = sys.stdin.readline

N = int(input()) 
M = int(input()) 

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

def dijkstra(graph, start, n):
    dist = [float('inf')] * (n + 1) 
    dist[start] = 0
    
    pq = [(0, start)]  
    
    while pq:
        d, u = heapq.heappop(pq)  
        
        if d > dist[u]:
            continue
        
        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v)) 
    
    return dist

dist = dijkstra(graph, start, N)
print(dist[end]) 