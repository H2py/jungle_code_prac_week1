import sys
from bisect import bisect_left
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

result = [arr[0], ]

for el in arr:
    if el > result[-1]:
        result.append(el)
    else:
        idx = bisect_left(result, el)
        result[idx] = el

print(len(result))