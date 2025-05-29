import sys
input = sys.stdin.readline

def bn_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            result.append(1)
            return
        elif arr[mid] > target :
            end = mid - 1
        else:
            start = mid + 1
    result.append(0)            
    return

n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))
result =[]

for tg in m_list:
    bn_search(n_list, tg, 0, len(n_list)-1)

print(' '.join(map(str, result)))


