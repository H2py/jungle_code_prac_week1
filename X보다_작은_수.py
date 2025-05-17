import sys
# sys.stdin = open("input.txt", "r")

n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

result_list = []
for num in a:
    if num < x:
        result_list.append(str(num))

print(' '.join(result_list))

#result = [str(num) for num in a if num < x]
#print(' '.join(result))
        