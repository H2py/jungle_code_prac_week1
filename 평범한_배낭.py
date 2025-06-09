import sys
input = sys.stdin.readline

N, K = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]

w,v = wv[0]
for i in range(K+1):
    if i >= w:
        dp[0][i] = v

for i in range(1, N):        
    weight, value = wv[i]
    
    for j in range(K+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[N-1][K])


import sys
input = sys.stdin.readline

N, K = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

for w, v in wv:
    for j in range(K, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[K])
