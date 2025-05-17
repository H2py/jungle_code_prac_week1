import sys

t = int(input())
input_list = []

for _ in range(t):
    input_list.append(int(sys.stdin.readline()))
    
input_list.sort()

for num in input_list:
    print(num)