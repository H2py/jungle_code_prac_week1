import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(input().strip()) for _ in range(N)]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

q = deque([(0,0,0,0)])
visited[0][0][0] = True

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

while q:
    x, y, broken, cnt = q.popleft()
    
    if x == N-1 and y == M-1:
        print(cnt + 1)
        sys.exit()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx <N and 0 <= ny <M:
            if not visited[nx][ny][broken] and matrix[nx][ny] == '0':
                visited[nx][ny][broken] = True
                q.append((nx, ny, broken, cnt+1))
            elif matrix[nx][ny] == '1' and broken == 0 and not visited[nx][ny][1]:
                visited[nx][ny][1] = True
                q.append((nx, ny, 1, cnt+1))             
print(-1)                