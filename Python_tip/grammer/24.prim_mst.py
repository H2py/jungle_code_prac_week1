import sys
import heapq
input = sys.stdin.readline

def prim_mst(V, graph):
    # 초기화
    visited = [False] * (V + 1)  # 방문 여부 (노드 1~V)
    heap = []  # 최소 힙: (가중치, 현재 노드, 다음 노드)
    total_weight = 0  # MST 가중치 합
    
    # 시작 노드 (1번 노드)
    visited[1] = True
    for v, w in graph[1]:
        heapq.heappush(heap, (w, 1, v))  # (가중치, u, v)
    
    # 프림 알고리즘
    while heap:
        weight, u, v = heapq.heappop(heap)
        if visited[v]:
            continue  # 사이클 방지
        visited[v] = True
        total_weight += weight
        # v의 이웃 간선 추가
        for next_v, next_w in graph[v]:
            if not visited[next_v]:
                heapq.heappush(heap, (next_w, v, next_v))
    
    # 모든 노드 방문 확인
    if sum(visited[1:V+1]) != V:
        return 0  # 비연결 그래프
    
    return total_weight

# 입력 처리 (백준 1197번)
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]  # 인접 리스트 (노드 1~V)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # 무방향 그래프

# MST 가중치 출력
print(prim_mst(V, graph))