import sys
sys.stdin = open('input.txt', 'r')
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

result = [0]

for el in arr:
    if el > result[-1]:
        result.append(el)
    else:
        left = 0
        right = len(result)
        
        while left < right:
            mid = (left + right) // 2
            if result[mid] < el:
                left = mid + 1
            else :
                right = mid
        result[right] = el

print(len(result))