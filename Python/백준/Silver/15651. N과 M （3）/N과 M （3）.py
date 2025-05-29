N, M = map(int,input().split())
answer = []

def dfs(depth):
    if depth == M:
        print(*answer)
        return
    for i in range(1, N+1):
        answer.append(i)
        dfs(depth+1)
        answer.pop()
        
dfs(0)