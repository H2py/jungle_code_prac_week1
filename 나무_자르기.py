import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def bs_search(start, end):
    best = 0
    while start <= end:
        mid = (start + end) // 2
        remains = sum(tree - mid for tree in trees if tree - mid > 0)

        if M > remains:
            end = mid - 1
        else:
            best = mid
            start = mid + 1

    return best            

N, M = map(int, input().split())
trees = sorted(list(map(int, input().split())))

print(bs_search(0, trees[-1]))
