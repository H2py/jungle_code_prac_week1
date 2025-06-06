import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
matrix = [[[0] * M for _ in range(N)] for _ in range(H)]

for h in range(H):
    for n in range(N):
        matrix[h][n] = list(map(int, input().split()))

dz = [0, 0, 0, 0, 1, -1]
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]

q = deque()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if matrix[z][y][x] == 1:
                q.append((z, y, x))

while q:
    z, y, x = q.popleft()
    
    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if matrix[nz][ny][nx] == 0:
                matrix[nz][ny][nx] = matrix[z][y][x] + 1
                q.append((nz, ny, nx))

max_day = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if matrix[h][n][m] == 0:
                print(-1)
                sys.exit()
            max_day = max(max_day, matrix[h][n][m])

print(max_day - 1)
