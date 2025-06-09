import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

di = [1] * N
dd = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            di[i] = max(di[i], di[j] + 1)
            
di_max = max(di)

for i in range(N):
    for j in range(i):
        if A[-(j+1)] < A[-(i+1)] :
            dd[-(i+1)] = max(dd[-(j+1)] + 1, dd[-(i+1)])

answer = 0
for i in range(N):
    answer = max(answer, di[i] + dd[i] - 1)

print(answer)
