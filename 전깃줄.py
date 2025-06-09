import sys
input = sys.stdin.readline

N = int(input())
pole = [tuple(map(int, input().split())) for _ in range(N)]
pole.sort()
dp = [1] * N

for i in range(N):
    for j in range(i):
        if pole[i][1] > pole[j][1]:
            dp[i] = max(dp[j] + 1, dp[i])

print(len(pole) - max(dp))