import sys
test = int(sys.stdin.readline())

for _ in range(test):
    a,b = map(int, sys.stdin.readline().split())
    print(f"{a+b}")

