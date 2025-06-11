import sys
input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]
dp = [[0] * (N+1) for _ in range(2)]
dp[1][1] = stairs[0]
dp[1][2] = stairs[1]
dp[0][2] = stairs[0] + stairs[1]

for i in range(3, N+1):
    dp[0][i] = dp[1][i-1] + stairs[i-1]
    dp[1][i] = max(dp[0][i-2], dp[1][i-2]) + stairs[i-1]

print(max(dp[0][N], dp[1][N]))
            
