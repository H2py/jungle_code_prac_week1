import sys
import math

def is_prime(n):
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True

test = int(sys.stdin.readline())

array = []
for _ in range(test):
    i = int(sys.stdin.readline())
    array.append(i)


for inputNum in array:
    a,b = inputNum//2, inputNum//2
    while(b<inputNum):
        if is_prime(a) and is_prime(b):
            print("{0} {1}".format(a, b))
            break
        else:
            a -=1
            b +=1
         