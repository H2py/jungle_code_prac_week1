import sys
# sys.stdin = open('input.txt', 'r')

def binary_search(arr, target, start, end) :
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            print(1)
            return 
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target :
            start = mid + 1
    print(0)    
    return

n = int(input())
first_list = list(map(int, input().split()))
m = int(input())
second_list = list(map(int, input().split()))

first_list.sort()

for num in second_list:
    binary_search(first_list, num, 0, len(first_list) - 1)