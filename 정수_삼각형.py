import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * (N) for _ in range(N)]
costs = [list(map(int, input().split())) for _ in range(N)]
dp[0][0] = costs[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + costs[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + costs[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + costs[i][j]
        
print(max(dp[N-1]))