import sys

input_list = []
for _ in range(9):
    input = int(sys.stdin.readline())
    input_list.append(input)

print(max(input_list))
print(input_list.index(max(input_list)) + 1)