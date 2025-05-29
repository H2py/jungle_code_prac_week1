str = input()
bomb = input()
stack = []

for s in str:
    stack.append(s)
    
    bomb_len = len(bomb)
    if stack[-bomb_len:] == list(bomb):
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
