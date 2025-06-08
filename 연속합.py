import sys
input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))
max_sum = current = dp[0]

for i in range(1, n):
    current = max(dp[i], current + dp[i])
    max_sum = max(max_sum, current)

print(max_sum)