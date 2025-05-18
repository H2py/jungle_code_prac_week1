import sys

inp = int(sys.stdin.readline())

input_list = [0] * 10001
for _ in range(inp):
    input_list[int(sys.stdin.readline())] += 1
    
for i, num in enumerate(input_list):
    for _ in range(num):
        print(i)