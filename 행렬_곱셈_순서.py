import sys
input = sys.stdin.readline

T = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(T)]
dp = [[0] * T for _ in range(T)]

for length in range(1, T):  
    for i in range(T - length):
        j = i + length
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][T-1])
