n = int(input())
cnt = 0
def print_hansu(num) :
    global cnt
    for n in range(1, num+1):
        if n < 100:
            cnt +=1
        elif n >= 100:
            a = n // 100
            b = (n % 100) // 10
            c = (n % 10)
            if a - b == b - c :
                cnt += 1
        elif n == 1000:
            break
            
    print(cnt)

print_hansu(n)