import sys
# sys.stdin = open('input.txt', 'r')
input_list = list(map(int, sys.stdin.readlines()))

for  in input_list:
    

input_list.sort()
print('\n'.join(map(str, input_list)))