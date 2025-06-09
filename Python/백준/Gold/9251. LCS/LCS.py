import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

N = len(str1)
M = len(str2)

dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(max(max(dp)))