import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 1, 0, -1]  
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]
shifts = []

for _ in range(K):
    cord = list(map(int, input().split()))
    board[cord[0] - 1][cord[1] - 1] = 1
    
L = int(input())
for _ in range(L):
    t, d = input().split()
    shifts.append((int(t), d))

i = 0
snake = deque([(0,0)])
board[0][0] = 2
direction = 0
x,y  = 0, 0
time = 0

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    time += 1
    
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        break
    
    if board[nx][ny] == 2:
        break
    
    
    if board[nx][ny] == 1:
        board[nx][ny] = 2
        snake.append((nx, ny))
    else:
        board[nx][ny] = 2
        snake.append((nx, ny))
        prev_x, prev_y = snake.popleft()
        board[prev_x][prev_y] = 0
    
    x, y = nx, ny
    
    if i < len(shifts) and time == shifts[i][0]:
        if shifts[i][1] == 'D':  
            direction = (direction + 1) % 4
        else:  
            direction = (direction - 1) % 4
        i += 1

print(time)    
