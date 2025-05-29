N, M = map(int, input().split())

def back_track(target, num):
    if num == target:
        return
    else:
        
    for i in range(1, N+1):
        back_track(target, i)        
    
[1]
[2]
[3]
[4]