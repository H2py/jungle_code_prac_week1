import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
matrix = [list(input().strip()) for _ in range(R)]
time = [[0] * C for _ in range(R)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

q = deque()
dochi_x, dochi_y = 0, 0                
dochi_time = 0

for i in range(R):
    for j in range(C):
        if matrix[i][j] == '*':
            q.append(('water', i, j))
        elif matrix[i][j] == 'S':
            dochi_x, dochi_y = i, j

q.append(('dochi', dochi_x, dochi_y))
            
while q :
    type, x, y = q.popleft()
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        
        if 0 <= nx < R and 0 <= ny < C:
            if type == 'water':
                if matrix[nx][ny] == '.':
                    matrix[nx][ny] = '*'
                    q.append(('water', nx, ny))
            elif type == 'dochi':
                if matrix[nx][ny] == 'D':
                    print(time[x][y]+1)
                    sys.exit()
                if matrix[nx][ny] == '.' and time[nx][ny] == 0:
                    time[nx][ny] = time[x][y] + 1
                    q.append(('dochi', nx, ny))
                        
                
print('KAKTUS')
    