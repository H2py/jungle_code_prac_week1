import sys
# sys.stdin = open('input.txt', 'r')        

n = int(input())
visited = [0] * n
visited[0] = True
min_cost = sys.maxsize
costs = [list(map(int, input().split()))for _ in range(n) ]

comb_list = []
for i in range(n):
    for j in range(n):
        if i != j :
            comb_list.append(costs[i][j])
            print(f"{i} {j}")
            

print(min_cost)

