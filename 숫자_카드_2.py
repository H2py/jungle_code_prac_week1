import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
n_list = sorted(map(int, input().split()))  

m = int(input())
m_list = list(map(int, input().split()))
result = {value : 0 for value in m_list}
def binary_search(arr, tg, start, end):
    while start <= end:
        mid = (start + end) // 2
        if tg == arr[mid]:
            result[tg] += 1
            return
        elif tg > arr[mid]:
            end = mid - 1
        else :
            start = mid + 1
    return 

sys.stdout.write(' '.join(map(str,result.values())))
