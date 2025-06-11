import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    grades = [tuple(map(int, input().split())) for _ in range(N)]
    grades.sort()
    cnt = 1
    best = grades[0][1]
    
    for i in range(1, N):
        if grades[i][1] < best:
            cnt +=1
            best = grades[i][1]
            
    print(cnt)