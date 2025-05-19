from itertools import permutations
import sys
# sys.stdin = open('input.txt', 'r')
test = int(input())
ls = list(map(int, input().split()))

all_list = list(permutations(ls))

max_list = []
for each_list in all_list:
    sum = 0
    for i in range(test - 1):
        sum += abs(each_list[i] - each_list[i+1])
    max_list.append(sum)
        
print(max(max_list))
        