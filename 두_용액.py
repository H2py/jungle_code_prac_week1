import sys
# sys.stdin = open('input.txt', 'r')
n = int(input())
liquids = list(map(int, sys.stdin.readline().split()))
liquids.sort()

start = 0
end = n - 1
min_sum = float('inf')
answer = []
while start < end:
    current_sum = liquids[start] + liquids[end]
    
    if abs(current_sum) < min_sum:
        min_sum = abs(current_sum)
        answer = [liquids[start], liquids[end]]
    
    if current_sum == 0:
        break
    elif current_sum < 0:
        start += 1
    else :
        end -= 1
        

print(f"{answer[0]} {answer[1]}")    
