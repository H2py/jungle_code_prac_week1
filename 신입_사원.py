import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    grades = [tuple(map(int, input().split())) for _ in range(N)]
    grades.sort(key=lambda x : x[1])
    cnt = 0
    
    for grade_i in range(N):
        grade1, grade2 = grades[grade_i]
        is_big = False
        for search_i in range(N):
            if grade_i == search_i:
                continue
            else:
                if grade1 < grades[search_i][0] or grade2 < grades[search_i][1]:
                    is_big = True
        if is_big :
            cnt +=1
    print(cnt)
    
    # 6 1
    # 4 2
    # 7 3
    # 1 4
    # 2 5
    # 3 6
    # 5 7
        