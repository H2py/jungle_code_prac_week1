n = int(input())

if n == 1:
    print(10)
elif n == 2:
    print(55)
else:
    dp = [0] * (n+1)
    dp[1] = 10
    dp[2] = 55
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] * (10+i-1) // i
    print(dp[n] % 10007)