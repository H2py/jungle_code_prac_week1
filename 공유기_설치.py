import sys
# sys.stdin = open('input.txt', 'r')
            
h, wifi = map(int, input().split())
houses = list(map(int, sys.stdin.readlines()))
houses.sort()

start, end = 1, houses[-1] - houses[0]
result = 0
while start <= end:
    mid = (start + end) // 2        
    res = []
    res.append(houses[0])
    
    for house in houses:
        if house - res[-1] >= mid:
            res.append(house)
    
    if len(res) >= wifi:
        result = mid
        start = mid+1

    else:
        end = mid-1

print(result)