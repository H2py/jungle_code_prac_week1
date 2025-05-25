import sys
input = sys.stdin.read

sys.setrecursionlimit(10**6)

def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    global cnt, result
    tmp = []
    i, j = p, q + 1

    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= q:
        tmp.append(arr[i])
        i += 1
    while j <= r:
        tmp.append(arr[j])
        j += 1

    for i in range(len(tmp)):
        cnt += 1
        arr[p + i] = tmp[i]
        if cnt == K:
            result = arr[p + i]

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
result = -1
merge_sort(A, 0, N - 1)
print(result)
