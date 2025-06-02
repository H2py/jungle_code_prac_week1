from collections import deque
import sys
input = sys.stdin.readline

cmp = int(input())
n = int(input())

graph = [[] for _ in range(cmp+1)]
visited = [False] * (n+1)

for _ in range(n):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(start):
    visited[start] = True
    queue = deque([start])
    count = 0
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count +=1
    return count

print(bfs(1))