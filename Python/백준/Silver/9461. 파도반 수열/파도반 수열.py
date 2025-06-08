import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    
    d = [0] * max((n+1), 11)
    d[1], d[2], d[3] = 1, 1, 1
    d[4], d[5], d[6] = 2, 2, 3
    
    for i in range(7, n+1):
        d[i] = d[i-1] + d[i-5]
        
    print(d[n])