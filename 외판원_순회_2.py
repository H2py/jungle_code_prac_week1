import sys

def tps(cur, cnt, cost):
    global min_cost
    
    if cnt == n and matrix[cur][0] != 0:
        min_cost = min(min_cost, cost + matrix[cur][0])
        return min_cost
    
    if cost >= min_cost:
        return
    
    for nxt in range(n):
        if not visited[nxt] and matrix[cur][nxt] != 0 :
            visited[nxt] = True
            tps(nxt, cnt+1, cost + matrix[cur][nxt])
            visited[nxt] = False


n = int(input())
matrix = [list(map(int, input().split()) for _ in range(n))]
min_cost = sys.maxsize
visited = [False] * n
visited[0] = True

tps(0, 1, 0)
print(min_cost)

