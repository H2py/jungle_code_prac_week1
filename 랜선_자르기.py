import sys
input = sys.stdin.readline

def bs_search(start, end):
    result = 0
    while start <= end:
        mid = (start+end+1) // 2
        target = sum(x // mid for x in ls)
    
        if target >= N:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    print(result)
    return
K, N = map(int, input().split())
ls = sorted(list(map(int, sys.stdin.readlines())))

bs_search(0, ls[-1])
        
