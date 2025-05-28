import sys
def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt, now = 1, mid + houses[0]
        
        for house in houses:
            if house >= now:
                cnt +=1
                now = house + mid
        
        if cnt >= wifi:
            start = mid + 1
        else:
            end = mid - 1
            
    return end
            
h, wifi = map(int, input().split())
houses = list(map(int, sys.stdin.readlines()))
houses.sort()

start, end = 1, (houses[-1] - houses[0]) 
print(binary_search(start, end))
# 1 2 4 8 9