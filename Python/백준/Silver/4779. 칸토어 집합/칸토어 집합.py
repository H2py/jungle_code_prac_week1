import sys
# sys.stdin = open('input.txt', 'r')

def cantor(n):
    if n == 0:
        return '-'
    
    left = cantor(n-1)
    space = ' ' * (3 ** (n-1))
    right = cantor(n-1)

    return left + space + right
inputs = list(map(int, sys.stdin.readlines()))

for num in inputs:
    print(cantor(num))