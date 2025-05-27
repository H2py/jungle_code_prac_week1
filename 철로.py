import sys
import heapq

input = sys.stdin.readline
n = int(input())
input_list = []

for _ in range(n):
    h, o = map(int, input().split())
    if h > o:
        heapq.heappush(input_list, [o, h])
    else :
        heapq.heappush(input_list, [h, o]) 
        
input_list.sort(key=lambda x: x[1])  

d = int(input())
hp = []
answer = 0

for start, end in input_list:
    if end - start > d:
        continue
    
    heapq.heappush(hp, start)
    
    while hp and hp[0] < end - d:
        heapq.heappop(hp)
    
    answer = max(answer, len(hp))

print(answer)
