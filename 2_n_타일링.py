N = int(input())
dp = [0] * max(N+1, 3)
dp[2] = 2

for i in range(3, N+1):
    if i % 2 == 0 :
        dp[i] = dp[i-1] + 2
    else:
        dp[i] = dp[i-1] + 1
print(dp[N])        