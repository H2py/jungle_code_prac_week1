from functools import cmp_to_key

def comparator(a,b):
    int1 = a+b
    int2 = b+a
    return ((int1 > int2) - (int1 < int2))

def solution(numbers):
    numbers = [str(n) for n in numbers]
    numbers = sorted(numbers, key=cmp_to_key(comparator), reverse=True)
    return str(int(''.join(numbers)))