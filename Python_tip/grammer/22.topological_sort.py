from collections import deque

def topological_sort(graph, n):
    # 1. 진입 차수 배열 초기화
    # 각 노드의 진입 차수 저장
    in_degree = [0] * n
    
    # 2. 진입 차수 계산
    # 모든 노드와 간선을 순회하며, 간선 (u -> v)에 대해 v 진입차수 증가
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
            
    # 3. 진입 차수가 0인 노드부터 시작
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    
    # 4. 큐에서부터 시작
    while queue:
        # 4-1. 노드를 꺼내 결과에 추가
        node = queue.popleft()
        result.append(node)
        
        # 4-2. 현재 노드에서 나가는 간선을 제거
        # 이웃노드 진입 차수 1 감소
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 5. 사이클 존재하는지 확인하기
    # 결과 리스트에 모든 노드가 추가되지 않았다면 사이클 존재
    if len(result) != n:
        return None
    
    return result            