import heapq  # 우선순위 큐를 사용하기 위해

def dijkstra(graph, start, n):
    # 거리 배열 초기화
    dist = [float('inf')] * n  # 모든 정점까지의 거리를 무한대로 설정
    dist[start] = 0  # 시작 정점의 거리는 0
    
    # 우선순위 큐: (거리, 정점)
    pq = [(0, start)]  # (거리, 정점) 쌍을 저장
    
    # 경로 추적을 위한 배열 (선택적)
    prev = [None] * n  # 각 정점에 도달하기 위해 직전에 방문한 정점
    
    while pq:
        # 가장 짧은 거리의 정점을 꺼냄
        d, u = heapq.heappop(pq)  # d: 현재까지의 거리, u: 현재 정점
        
        # 이미 처리된 정점이면 스킵 (더 짧은 경로가 이미 발견된 경우)
        if d > dist[u]:
            continue
        
        # u에서 연결된 모든 이웃 정점 v를 탐색
        for v, weight in graph[u]:  # v: 이웃 정점, weight: 간선 가중치
            # u를 거쳐 v로 가는 거리
            new_dist = dist[u] + weight
            
            # 더 짧은 경로를 발견한 경우
            if new_dist < dist[v]:
                dist[v] = new_dist  # 거리 갱신
                prev[v] = u  # 경로 추적: v에 도달하기 위해 u를 거침
                heapq.heappush(pq, (new_dist, v))  # 새로운 거리로 큐에 추가
    
    return dist, prev

# 경로 재구성 함수
def get_path(prev, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = prev[current]
    return path[::-1]  


n = 5  
graph = [
    [(1, 4), (2, 8)],           
    [(0, 4), (2, 2), (3, 5)],   
    [(0, 8), (1, 2), (3, 4), (4, 3)],
    [(1, 5), (2, 4), (4, 6)],
    [(2, 3), (3, 6)]
]

start = 0
dist, prev = dijkstra(graph, start, n)

# 결과 출력
print("시작 정점 0에서 각 정점까지의 최단 거리:")
for i in range(n):
    print(f"정점 {i}: {dist[i]}")

# 특정 경로 출력 (예: 0 -> 4)
end = 4
path = get_path(prev, end)
print(f"정점 0에서 {end}로 가는 최단 경로: {path}")