import sys
# sys.stdin = open('input.txt', 'r')

paren = sys.stdin.readline().strip()
stack = []
is_valid = True

for p in paren:
    if p == '(' or p == '[':
        stack.append(p)
    elif p == ')':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                if temp == 0:
                    stack.append(2)
                else:
                    stack.append(temp * 2)
                break
            elif isinstance(top, int):
                temp += top
            else:
                is_valid = False
                break
        else:
            is_valid = False
            break
    elif p == ']':
        temp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(temp * 3)
                break
            elif isinstance(top, int):
                temp += top
            else:
                is_valid = False
                break
        else:
            is_valid = False
            break

if not is_valid :
    print(0)
else:
    sum = 0
    for s in stack:
        if isinstance(s, int):
            sum += s
        else:
            sum = 0
            break
    print(sum)