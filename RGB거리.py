import sys
input = sys.stdin.readline

T = int(input())
colors = [tuple(map(int, input().split())) for _ in range(T)]

dp = [[0] * 3 for _ in range(T)]

dp[0][0], dp[0][1], dp[0][2] = colors[0]

for i in range(1, T):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + colors[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + colors[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + colors[i][2]
    
print(min(dp[T-1]))
