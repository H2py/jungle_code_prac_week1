import sys
x, y, w, h = map(int, sys.stdin.readline().split())

a = x
b = y
c = w - x
d = h - y

print(min(a,b,c,d))