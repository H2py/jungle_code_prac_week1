import sys
# sys.stdin = open('input.txt', 'r')

num, row, col = map(int, input().split())
total = 0
lo = (2**num)
def find_z(n,r,c):
    global total, lo
    total += 1
    if(n == 1): 
        print(total)
        return
    else :
        n-=1
        lo /= 2
        find_z(n,r,c)
        find_z(n,r,c+lo)
        find_z(n,r+lo,c)
        find_z(n,r+lo,c+lo)
find_z(num, row, col)