import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
      
        if arr[mid] == target:
            sys.stdout.write(str(1) + '\n')
            return
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    sys.stdout.write(str(0) + '\n')
    return

N = int(input())
A = list(map(int, input().split()))

M = int(input())
tg_list = list(map(int, input().split()))
A.sort()

for el in tg_list:
    binary_search(A, el, 0, len(A) - 1)