import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j):
    visited[i][j] = True
    queue = deque([(i, j)])
    matrix[i][j] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and matrix[nx][ny] == 1:
                    visited[nx][ny] = True
                    matrix[nx][ny] = 0
                    queue.append((nx, ny))

T = int(input())
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(T):
    M, N, K = map(int, input().split())
    
    matrix = [[0] * (M+1) for _ in range(N+1)]
    visited = [[False] * (M+1) for _ in range(N+1)]
    cnt = 0
    
    for _ in range(K):
        u,v = map(int, input().split())
        matrix[v][u] = 1
                
    for i in range(N+1):
        for j in range(M+1):
            if not visited[i][j] and matrix[i][j] == 1:
                bfs(i, j)
                cnt +=1
    print(cnt)

    
