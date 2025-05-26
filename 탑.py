import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
heights = list(map(int, sys.stdin.readline().split()))

stack = []
result = [0] * N

for i in range(N-1, -1, -1):
    while stack and heights[i] > stack[-1][1]:
        result[stack[-1][0]] = i + 1
        stack.pop()
    stack.append((i, heights[i]))
    
print(*result)
