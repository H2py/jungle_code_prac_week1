import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(i, j):
    visited[i][j] = True
    queue = deque([(i, j, 0)])
    
    while queue:
        x, y, dist = queue.popleft()

        if matrix[x][y] == 1:  
            return dist
        
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
    
            if 0 <= nx < N and 0 <= ny < N : 
                if not visited[nx][ny]:
                    visited[nx][ny] = True            
                    queue.append((nx,ny, dist+1))
 

T = int(input())

for _ in range(T):
    N = int(input())
    visited = [[False] * (N+1) for _ in range(N+1)]
    matrix = [[0] * (N+1) for _ in range(N+1)]
    
    s_x, s_y = map(int,input().split())
    e_x, e_y = map(int,input().split())
    
    matrix[e_x][e_y] = 1
    
    print(bfs(s_x, s_y))