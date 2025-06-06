import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

q = deque()                
                    
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            q.append((i,j))                        
            
while q :
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                q.append((nx,ny))

max_day = 0                
for row in matrix:
    for val in row:
        if val == 0:
            print(-1)
            sys.exit(0)
        else:
           max_day = max(max_day, val) 
print(max_day - 1)                            