import sys
# sys.stdin = open('input.txt', 'r')
input = str(input())
cnt = 0

def add_cicle(num, cnt):
    if num == '0':
        return cnt
    elif int(num) < 10:
        a, b = 0, int(num) 
    else:
        a,b = int(num[0]), int(num[1])
    
    sum_num = a + b
    str_num = str(sum_num)
    
    if len(str_num) > 1:
        new_num = str(b) + str_num[1]
    else:
        new_num = str(b) + str_num
    
    if int(new_num) == int(input):
        return cnt
    return add_cicle(new_num, cnt+1)


print(add_cicle(input, 1))


