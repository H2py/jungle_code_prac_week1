import sys
from itertools import combinations

n = list(map(int, sys.stdin.readlines()))

h_sum = sum(n)
find = []
for i in combinations(n, 2):
    if h_sum - sum(i) == 100:
        find = i
        break
    
for i in find:
    n.remove(i)
n.sort()

for h in n:
    print(h)