import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

queue = deque()
output = []  

for _ in range(n):
    inp = input().split()
    cmd = inp[0]
    
    if cmd == 'push':
        queue.append(inp[1])
    elif cmd == 'front':
        output.append(str(queue[0] if queue else -1))
    elif cmd == 'back':
        output.append(str(queue[-1] if queue else -1))
    elif cmd == 'pop':
        output.append(str(queue.popleft() if queue else -1))
    elif cmd == 'empty':
        output.append(str(1 if not queue else 0))
    elif cmd == 'size':
        output.append(str(len(queue)))

sys.stdout.write('\n'.join(output))