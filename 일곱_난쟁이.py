import sys
from itertools import combinations

n = list(map(int, sys.stdin.readlines()))

for i in combinations(n, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break