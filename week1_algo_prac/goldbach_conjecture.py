import sys
import math

def is_prime(n):
    for j in range(2, math.sqrt(n) + 1):
        if n % j == 0:
            return False
    return True

test = int(sys.stdin.readline())

array = []
for i in range(0, test):
    i = int(sys.stdin.readline())
    array.append(i)

array.sort()

for i in range(array):
    a,b = array//2, array//2
    if is_prime(a) and is_prime(b):
        print("{0} {1}".format(a, b))
    else:
        a -=1
        b +=1
         
