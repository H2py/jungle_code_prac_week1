N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0
def checkSum(x, y, n):
    color = matrix[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != matrix[i][j]:
                return -1
    
    return color

def split(x, y, n):
    global blue, white
    
    if checkSum(x,y,n) == -1:
        split(x, y, n//2)
        split(x + n//2, y, n//2)
        split(x, y + n//2, n//2)
        split(x + n//2, y + n//2, n//2)
    elif checkSum(x,y,n) == 1:
        blue +=1
    else :
        white +=1
        
        
split(0, 0, N)
print(white)
print(blue)
        
    