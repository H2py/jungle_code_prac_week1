import sys
from itertools import permutations
# sys.stdin = open('input.txt', 'r')

def add_permu(cont, total):
    global cnt
    
    if total == target:
        for i in range(n):
            temp = []
            if visited[i]:
                temp.append(input_list[i])
        memo.append(temp)
        cnt +=1
        return
    
    if cont == n :
        return 
    
    for nxt in range(n):
        if not visited[nxt] and not memo[nxt] in memo:
            visited[nxt] = True
            add_permu(cont+1, total + input_list[nxt])
            visited[nxt] = False
    

# for i in range(1,n):
#     print(sum(input_list[:i]))
#     if sum(input_list[:i]) == target:
#         cnt+=1

# for permu in permutations(input_list, n):
#     print(permu)

cnt = 0
n, target = map(int, input().split())
input_list = list(map(int, input().split()))
visited = [False] * n
memo = []
add_permu(0, 0)
print(cnt)

    
