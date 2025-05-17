import sys

n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

result_list = []
for num in a:
    if num < x:
        result_list.append(str(num))

print(' '.join(result_list))