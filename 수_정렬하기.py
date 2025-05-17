import sys
t = int(sys.stdin.readline())

input_list = []
for _ in range(t):
    v = int(sys.stdin.readline())
    input_list.append(v)

input_list.sort()
for num in input_list:
    print(num)