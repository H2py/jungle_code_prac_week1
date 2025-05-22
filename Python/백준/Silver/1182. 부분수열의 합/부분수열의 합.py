def dfs(index, total):
    global cnt
    if index == n:
        if total == target:
            cnt +=1
        return
    dfs(index+1, total)
    dfs(index+1, total+input_list[index])


cnt = 0
n, target = map(int, input().split())
input_list = list(map(int, input().split()))

dfs(0,0)
if target == 0:
    cnt -= 1
    
print(cnt)