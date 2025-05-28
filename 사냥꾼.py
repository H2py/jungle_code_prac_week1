import sys
input = sys.stdin.readline
M, N, L = map(int, input().split())
cord_x = map(int, input().split())
board = [[0] * (N+2) for _ in range(N+2)]

animals = [list(map(int, input().split())) for _ in range(N)]
for x, y in animals:
    board[x][y] = 1
    
for x in cord_x:
    board[x][0] = 2
print(board)

[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [2, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
 [2, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
 [2, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

