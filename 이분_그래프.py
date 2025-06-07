import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V+1)]
    
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append((v, 'blue')) # 정점이랑 현재 color 입력 받음
    
    q = deque([(1, 'blue')])        
    


    