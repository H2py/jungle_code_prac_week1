import heapq, sys
input = sys.stdin.readline

N = int(input())
info = [tuple(map(int, input().split())) for _ in range(N)]
info.sort(key = lambda x : (x[2], x[1]))
# 강의 번호, 강의 시작 시간, 강의 종료 시간

meet_room_cnt = 1
meet_room_num = 1
# 필요한 강의실 개수 판별
# 강의실 번호 판별

for i in range(1, N):
    result = [(info[0], 1)]
    for j in range(N-i):
        prev_n, prev_s, prev_e = result[-1]
        cur_n ,cur_s, cur_e = info[j]
        
        if prev_e <= cur_s :
            heapq.heappush(result, (info[j], meet_room_num))
        else:
            meet_room_cnt += 1
            continue
    meet_room_num += 1

for i in range(N):
    print(heapq.heappop(result)[3])

# 1 3 8   1
# 2 7 13  2
# 3 2 14  3
# 4 12 18 1
# 5 6 20  4
# 6 15 21 2
# 7 20 25 1
# 8 6 27  5

# 첫째 줄에는 필요한 최소 강의실 개수 K를 출력한다. 
# 둘째 줄부터 N개의 줄에 걸쳐, 
# 1번부터 N번까지의 강의에 배정할 강의실 번호를 순서대로 출력한다. 
# 편의상 강의실 번호는 1, 2, ..., K로 매긴다. 단, 가능한 답이 여러 개일 경우, 그 중 아무 거나 출력한다. 

