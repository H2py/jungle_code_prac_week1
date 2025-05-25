import sys
stack = []
n = int(input())
input_list = list(map(int, sys.stdin.readlines()))
for input in input_list:    
    if input != 0 :
        stack.append(input)
    else:
        stack.pop()
        
print(sum(stack))