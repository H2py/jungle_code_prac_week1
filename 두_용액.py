import sys
input = sys.stdin.readline

n = int(input())
liquids = sorted(list(map(int, input().split())))
start = 0
end = n-1

min_sum = float('inf')
answer = [liquids[start], liquids[end]]

while start < end:
    cur_sum = liquids[start] + liquids[end]
    
    if abs(cur_sum) < min_sum:
        min_sum = abs(cur_sum)
        answer = [liquids[start], liquids[end]]
        if min_sum == 0:
            break
    if cur_sum < 0:
        start +=1
    else:
        end -=1
    
print(f"{answer[0]} {answer[1]}")
        
        

