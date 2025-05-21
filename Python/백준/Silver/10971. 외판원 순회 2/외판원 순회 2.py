import sys
# sys.stdin = open('input.txt', 'r')
def tsp(cur, cnt, cost):
    global min_cost
    
    if cnt == n and distance[cur][0] != 0:
        min_cost = min(min_cost, cost + distance[cur][0])
        return
    
    
    for nxt in range(n):
        if distance[cur][nxt] != 0 and not visited[nxt]:
            visited[nxt] = True
            tsp(nxt, cnt+1, cost+distance[cur][nxt])
            visited[nxt] = False
    
    
n = int(input())
distance = [list(map(int, input().split())) for _ in range(n)]
min_cost = sys.maxsize
visited = [False] * n
visited[0] = True

tsp(0,1,0)
print(min_cost)