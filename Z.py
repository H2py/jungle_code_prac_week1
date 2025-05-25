import sys
# sys.stdin = open('input.trt', 'r')
num, row, col = list(map(int, input().split()))

def z(n, r, c):
    global cnt
    if n == 0 :
        return

    half = 2**(n-1)
    area = half * half


    if row < r + half and col < c + half:
        z(n-1, r, c)
    elif row < r + half and col >= c + half:
        cnt += area
        z(n-1, r, c + half)
    elif row >= r + half and col < c + half:
        cnt += 2*area
        z(n-1, r+ half, c)
    else:
        cnt += 3*area
        z(n-1, r + half, c + half)

    
cnt = 0    
z(num, 0, 0)
print(cnt)