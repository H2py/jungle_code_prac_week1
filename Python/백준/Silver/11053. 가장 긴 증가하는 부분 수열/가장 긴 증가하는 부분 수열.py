n = int(input())
arr = list(map(int, input().split()))

result = [0]

for el in arr:
    if el > result[-1]:
        result.append(el)
    else:
        start = 0
        end = len(result) - 1
        while start < end:
            mid = (start + end) //2
            if result[mid] < el:
                start = mid + 1
            else:
                end = mid
        result[end] = el

print(len(result) - 1)
        