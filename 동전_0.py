import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = list(map(int, sys.stdin.readlines()))
coins.sort(reverse=True)
result = []

for i in range(N):
    cnt = 0
    temp = K
    for coin in coins[i:]:
        if temp == 0:
            result.append(cnt)
            break
        cnt += temp // coin
        temp %= coin

print(min(result))