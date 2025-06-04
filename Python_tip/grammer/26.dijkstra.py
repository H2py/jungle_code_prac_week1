import heapq

def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
        
        for v, weight in graph[u]:
            new_dist = weight + dist[u]
            
            if new_dist < dist[v]:
                dist[v] = new_dist  # 거리 갱신
                heapq.heappush(pq, (new_dist, v))  # 새로운 거리로 큐에 추가