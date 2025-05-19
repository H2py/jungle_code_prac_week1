import sys
import math
# sys.stdin = open('input.txt', 'r')

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 :
            return False
    return True

n = int(input())

input_list = []
for _ in range(n):
    i = int(sys.stdin.readline())
    input_list.append(i)

for num in input_list:
    if num % 2 == 0 :
        a, b = num//2, num//2
            
        while(b < num) :
            if is_prime(a) and is_prime(b) :
                print(f"{a} {b}")
                break
            else:
                a -= 1
                b += 1