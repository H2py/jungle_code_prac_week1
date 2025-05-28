import sys
input = sys.stdin.readline
n = int(input())
ls = list(map(int, input().split()))

answer = [0]
for el in ls:
    if el > answer[-1]:
        answer.append(el)
    else:
        start, end = 0, len(answer) - 1
        while start < end:
            mid = (start + end) // 2
            
            if answer[mid] < el:
                start = mid + 1
            else:
                end = mid
        answer[start] = el

print(len(answer) - 1)