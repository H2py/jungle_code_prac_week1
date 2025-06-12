import sys
N = int(input())
cnt = 0

if N < 2 or N == 3:
    print(-1)
    sys.exit()

cnt += N // 5
N %= 5

if N % 2 == 1:
    cnt -= 1
    N += 5
    cnt += N // 2
    N %= 2
    
    if N == 0 :
        print(cnt)
    else:
        print(-1)
else:
    cnt += N//2
    N %= 2
    
    if N == 0 :
        print(cnt)
    else:
        print(-1)
    
    
