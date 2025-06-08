import sys
input = sys.stdin.readline

n = int(input())
dp = [0]
temp = list(map(int, input().split()))
dp += temp

for i in range(n):
    if dp[i] > 0 and dp[i] + dp[i+1] > 0:
        dp[i+1] += dp[i]
dp.pop(0)
print(max(dp))