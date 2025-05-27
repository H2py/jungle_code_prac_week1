import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

ls = [x for x in range(1, n+1)]
dq = deque(ls)

while len(dq) > 1:
    dq.popleft()
    temp = dq.popleft()
    dq.append(temp)
    
print(dq[0])