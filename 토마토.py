import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()
for i in range(M):
    for j in range(N):
        for k in range(H):
            if matrix[i][j][k] == 0:
                q.append((i, j, k))
                
print(matrix)                