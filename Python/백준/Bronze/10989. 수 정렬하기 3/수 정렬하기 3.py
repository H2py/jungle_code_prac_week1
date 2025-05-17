import sys
input = int(sys.stdin.readline())

input_array = [0] * 10001
while(input > 0):
    input_array[int(sys.stdin.readline())] += 1
    input -= 1

for i, n in enumerate(input_array):
    for _ in range(n):
        print(i)