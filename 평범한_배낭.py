import sys
input = sys.stdin.readline

N, K = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(N):
    w, v = wv[i]
    for j in range(K + 1):
        if j < w:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w] + v)

print(dp[N][K])



import sys
input = sys.stdin.readline

N, K = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

for w, v in wv:
    for j in range(K, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[K])
