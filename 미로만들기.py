import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

n = int(input())
matrix = [list(map(int, input().strip())) for _ in range(n)]  
change_matrix = [[INF] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()
q.append((0,0))
change_matrix[0][0] = 0

while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if matrix[nx][ny] == 1:
                cost = change_matrix[x][y]
            else:
                cost = change_matrix[x][y] + 1
            if cost < change_matrix[nx][ny]:
                change_matrix[nx][ny] = cost
                
                if matrix[nx][ny] == 1:
                    q.appendleft((nx,ny))
                else:
                    q.append((nx,ny))
                    
print(change_matrix[n-1][n-1])                    