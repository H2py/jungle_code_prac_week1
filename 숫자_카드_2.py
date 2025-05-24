from sys import stdin

A, B = stdin.read().split('\n')[1::2]
A = list(A.split())
B = B.split()
print(''.join('1 ' if str(x) in A else '0 ' for x in B))