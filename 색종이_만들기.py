N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0

def div_conq(arr):
    global white, blue
    
    