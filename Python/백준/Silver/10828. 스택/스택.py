import sys
num = int(input())
stack = []
for _ in range(num):
    inp = sys.stdin.readline().split()
    cmd = inp[0]
    el = int(inp[1]) if len(inp) > 1 else ''
    
    if cmd == 'push':
        stack.append(el)
        
    elif cmd == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif cmd == 'size':
        print(len(stack))
    elif cmd =='empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)