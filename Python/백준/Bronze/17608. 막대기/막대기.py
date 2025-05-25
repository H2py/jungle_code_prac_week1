import sys
# sys.stdin = open('input.txt', 'r')
n = int(input())
stack = list(map(int, sys.stdin.readlines()))
stack.reverse()
result = [stack[0]]

for el in stack[1:]:
    if result[-1] < el:
        result.append(el)

print(len(result))