import sys
# sys.stdin = open('input.txt', 'r')
test = int(input())
input_list = list(map(int, sys.stdin.readlines())) 

arr = [0] * 11
arr[1], arr[2], arr[3] = 1, 2, 4

for i in range(4, 11):
    arr[i] = arr[i-3] + arr[i-2] + arr[i-1]

for num in input_list:
    print(arr[num])



    
# 1+1+1+1 num == 4일때,
# 