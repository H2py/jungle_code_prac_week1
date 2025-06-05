import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

matrix = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

result = []

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(i, j):
    q = deque([(i, j)])
    matrix[i][j] = 0
    visited[i][j] = True
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and matrix[nx][ny] == 1:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx, ny))
    result.append(cnt)
    
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

print(len(result))
for value in sorted(result):
    print(value)
