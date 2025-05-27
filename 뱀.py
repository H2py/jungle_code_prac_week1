import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]  
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

L = int(input())
shifts = []
for _ in range(L):
    t, d = input().split()
    shifts.append((int(t), d))

time = 0
direction = 0
i = 0
x, y = 0, 0
snake = deque([(0, 0)])
board[0][0] = 2 

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    time += 1

    if nx < 0 or ny < 0 or nx >= N or ny >= N:
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

    if i < len(shifts) and shifts[i][0] == time: 
        if shifts[i][1] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        i += 1

print(time)
