import sys
sys.stdin = open('input.txt', 'r')
n, r, c = list(map(int, input().split()))

def z(n, x, y):
    if n == 0:
        return
    
    half =2**(n-1)
    area = half * half

    if r < x + half and c < y + half:
        return z(n-1, c, r)
    elif 
        z(n-1, c + half, r)
        z(n-1, c , r + half)
        z(n-1, c + half, r + half)
    

print(z(n,0,0))
