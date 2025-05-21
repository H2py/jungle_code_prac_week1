import math
def nsum(n):
    if n == 0:
        return 0
    return n+ nsum(n-1)


# tail recursion에 대해서 공부하기 sum for문이랑 차이가 있는가?
# return n + nsum(n-1) vs return nsum(n-1, total + n)


def exp_t(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return b**2 * exp_t(b, n/2)
    else:
        return b * exp_t(b, n-1)
    
    
def fib(n):
    if n < 2:
        return 1
    
    return fib(n-1) + fib(n-2) 


a = [1,2,3]
def cc(c_list, total):
    money = 4
    for change in c_list:
        div = money / change