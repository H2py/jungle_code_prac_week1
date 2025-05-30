N, M = map(int, input().split())
answer = []

def dfs(start, depth):
    if depth == M :
        print(*answer)
        return
    
    for i in range(start, N+1):
        answer.append(i)
        dfs(i + 1, depth+1)
        answer.pop()
        
dfs(1,0)       