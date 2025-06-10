import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x : (x[1], x[0]))
result = []
result.append(meetings[0])

for i in range(1, N):
    cur_s, cur_e = meetings[i]
    prev_s, prev_e = result[-1]
    
    if cur_s >= prev_e:
        result.append((cur_s, cur_e))
        
print(len(result))        