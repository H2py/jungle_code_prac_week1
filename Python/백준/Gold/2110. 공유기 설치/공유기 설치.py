# 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 
#C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 
#둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

import sys

house, wifi = map(int, input().split())
cords = list(map(int, sys.stdin.readlines()))
cords.sort()
result = 0
start, end = 1, cords[-1] - cords[0] 

while start <= end:
    res = []
    res.append(cords[0])
    mid = (start + end) // 2
    
    for cord in cords:
        if cord - res[-1] >= mid:
            res.append(cord)
            
    if len(res) >= wifi:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(result)        