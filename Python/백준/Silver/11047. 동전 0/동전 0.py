import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = list(map(int, sys.stdin.readlines()))
coins.sort(reverse=True)
result = []

for i in range(N):
    cnt = 0
    k = K
    for coin in coins[i:]:
        if k == 0:
            break
        cnt += k // coin
        k %= coin
    result.append(cnt)
    
print(min(result))