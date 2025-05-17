import sys
# sys.stdin = open('input.txt', 'r')
test = int(sys.stdin.readline())

input_list = []
for _ in range(test):
    input = str(sys.stdin.readline())
    input_list.append(input)
    
for str in input_list:
    sum = 0
    next = 0
    for i in str:
        if i == 'O':
            sum += 1 + next
            next += 1
        elif i == 'X':
            next = 0
        else : break
    print(sum)