import sys
import math

def is_prime(n):
    for i in (2, int(math.sqrt(n))+1):
        if n % i == 0 :
            return False
    return True

t = int(sys.stdin.readline())

numArrayList = []
for _ in range(t):
    i = int(sys.stdin.readline())
    numArrayList.append(i)
    
for num in numArrayList:
    a, b = num//2, num//2
    while(b < num):
        if is_prime(a) and is_prime(b):
            print('{0} {1}'.format(a, b))
            break
        else:
            a -=1
            b +=1
        