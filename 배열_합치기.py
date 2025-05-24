import sys
# sys.stdin = open('input.txt', 'r')
LN, RN = map(int, input().split())
left_arr = list(map(int, sys.stdin.readline().split()))
right_arr = list(map(int, sys.stdin.readline().split())) 


def merge(l_arr, r_arr):
    result = []
    i = j = 0
    while i < len(l_arr) and j < len(r_arr):
        if l_arr[i] < r_arr[j]:
            result.append(l_arr[i])
            i +=1
        else :
            result.append(r_arr[j])
            j +=1
    
    result.extend(l_arr[i:])
    result.extend(r_arr[j:])
    
    return result

print(*merge(left_arr, right_arr))