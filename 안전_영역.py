import sys
# sys.stdin = open('input.txt', 'r')

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n = int(input())
height_matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [list(map(bool, [False] * n )) for _ in range(n)]
group_matrix = [list(map(int, [0] * n)) for _ in range(n)]

def find_safe_area(x, y, h, cnt):
    if x < 0 or y < 0 or x >= n or y >= n or visited[x][y] or h < n:
        return
    
    visited[x][y] = True
    
    if group_matrix[x][y] == 0:
        group_matrix[x][y] = cnt
        return    
    
    for i in range(4):
        if visited[x+dx[i]][y+dy[i]] == False:
            find_safe_area(x+dx[i], y+dy[i], height_matrix[x+dx[i]][y+dy[i]], cnt+1)

find_safe_area(0,0,n,1)
print(max(group_matrix))