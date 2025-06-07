import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    coins = [map(int, input().split())]
    target = int(input())
    
    d = [0] * (N+1)
    
    for coin in coins:
        d[coin] = 1
    
    for i in range(2, N+1):
        if i % coin == 0:
            d[i] = max(d[i], d[i-coin] + d[coin])
    
    
    