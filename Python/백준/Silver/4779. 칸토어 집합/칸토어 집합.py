import sys
# sys.stdin = open('input.txt', 'r')

cantor_list = []
def cantor(n):
    if n == 0:
        cantor_list.append('-')
        return
    
    cantor(n-1)
    for _ in range((3**n) // 3):
        cantor_list.append(' ')
    cantor(n-1)

inputs = list(map(int, sys.stdin.readlines()))


for num in inputs:
    cantor(num)
    print(''.join(cantor_list))
    cantor_list.clear()