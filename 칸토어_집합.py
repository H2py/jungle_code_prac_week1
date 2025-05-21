import sys
sys.stdin = open('input.txt', 'r')

def contoar(n):
    if n == 0:
        print('-')
        return
    

inputs = list(map(int, sys.stdin.readlines()))



print(inputs)