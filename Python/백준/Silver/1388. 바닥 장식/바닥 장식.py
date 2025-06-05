
import sys
sys.setrecursionlimit(10*6)
input = sys.stdin.readline

# 세로크기 n, 가로크기 m
n,m = map(int, input().split())

# 패턴 저장할 floor
floor = []
# 방문 여부 확인할 visited
visited = []

# 배열 채워넣기
for _ in range(n):
    floor.append(list(input().strip()))
    visited.append([0] * m)

def fun(x,y):
    # 방문 표시
    visited[x][y] = 1
    current = floor[x][y]

    if current == '-':
        ny = y + 1
        # n범위안에 들고, 방문하지 않고, 패턴이 -일 때
        if ny < m and visited[x][ny] == 0 and floor[x][ny] == "-" :
            fun(x, ny)

    if current == "|":
        nx = x + 1
        # m범위 안에 들고, 방문하지 않고, 패턴이 |일 때
        if nx < n and visited[nx][y] == 0 and floor[nx][y] == "|":
            fun(nx, y)

count = 0

# 각 칸을 돌면서 실행
for i in range(n):
    for j in range(m):
        # 방문하지 않았다면
        if visited[i][j] == 0:
            fun(i,j)
            count += 1

print(count)