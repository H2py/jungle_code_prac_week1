import sys

test = int(sys.stdin.readline())

for _ in range(test):
    n, s = input().split()
    n = int(n)
    s = s.strip()
    
    result = ''
    for string in s:
        for _ in range(n):
            result += string
    print(result)
    
