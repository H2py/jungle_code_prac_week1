def solution(h_arr, h):
    cnt = 0
    for f in h_arr:
        if f > h:
            cnt +=1
    return cnt