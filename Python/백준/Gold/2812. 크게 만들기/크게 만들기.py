import sys
# sys.stdin = open('input.txt', 'r')

total, sub_num = map(int, input().split())
input_str = str(input())
stack = []

remain = total - sub_num

for el in input_str:
    while sub_num > 0 and stack and stack[-1] < el:
        stack.pop()
        sub_num -= 1
    stack.append(el)

result = ''.join(stack[:remain])
print(result)