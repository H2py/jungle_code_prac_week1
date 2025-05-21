import sys
input = int(sys.stdin.readline())

def hanoi(start, end, inter, n):
    if n == 1:
        print(f"{start} {end}")
    else:
        hanoi(start, inter, end, n-1)
        print(f"{start} {end}")
        hanoi(inter, end, start, n-1)
    
print(2**input - 1)
hanoi(1,3,2,input)