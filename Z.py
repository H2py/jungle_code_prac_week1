import sys
# sys.stdin = open('input.txt', 'r')

num, row, col = map(int, input().split())
total = 0
side = (2**num)
def find_z(n,r,c):
    global total, side
    total+=1
    if(n == 0): 
        return 0
    else :
        side //= 2
        find_z(n-1,r,c)
        find_z(n-1,r,c+side)
        find_z(n-1,r+side,c)
        find_z(n-1,r+side,c+side)
find_z(0, 0, col)
print(total)


# n=3일 때, 재귀적으로 그려줄 4가지를 다시 출력할 것이다
# side(변의 길이) = 8 // 2
# 1.find_z(n-1, r, c)
# 2.find_z(n-1, r, c+side)
# 3.find_z(n-1, r + side, c)
# 4.find_z(n-1, r+side, c+side)

# 다음 호출 시, 
# find_z(2, r, c)  
# find_z(2, r, c+4)  
# find_z(2, r+4, c)  
# find_z(2, r+4, c+4)  