import sys
# sys.stdin = open('input.txt', 'r')

input = int(sys.stdin.readline())

def make_star(n):
    if n == 3:
        print('***')
        print('* *')
        print('***')
    
    return 9 * make_star(n // 3)

make_star(input)