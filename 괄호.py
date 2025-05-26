import sys
n = int(sys.stdin.readline())

for _ in range(n):
    parenthesis = sys.stdin.readline().strip()
    stack = []
    is_valid = True
    
    for p in parenthesis:
        if p == '(':
            stack.append(p)
        else:
            if stack :
                stack.pop()
            else:
                is_valid = False
                break
            
    if is_valid and not stack: print('YES')
    else : print('NO')
