import sys
input = sys.stdin.readline

n, wifi = map(int, input().split())
houses = sorted(list(map(int,sys.stdin.readlines())))

start, end = 1, houses[len(houses) - 1] - houses[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    done = [houses[0]]
    
    for i in range(1, n):
        if houses[i] - done[-1] >= mid:
            done.append(houses[i])
            
    if len(done) >= wifi:
        answer = mid
        start = mid +1
    else:
        end = mid -1
        
