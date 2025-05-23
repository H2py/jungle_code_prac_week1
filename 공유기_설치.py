import sys

def binary(arr, left, right):
    global cnt
    while left <= right or cnt == c:
        mid = (left + right) // 2
        c_list.append(mid)
        cnt += 1
        
        binary(arr, left, mid - 1)
        binary(arr, mid + 1, right)
        
    return None

n, c = map(int, input().split())
x_list = list(map(int, sys.stdin.readlines()))
x_list.sort()
c_list = []
cnt = 0

binary(x_list, 0, len(x_list) - 1)
print(max([c_list[i] - c_list[i-1] for i in range(1, c)]))