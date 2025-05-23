from sys import stdin

A, B = stdin.read().split('\n')[1::2]
A = set(A.split())
B = B.split()
print(''.join('1 ' if x in A else '0 ' for x in B))