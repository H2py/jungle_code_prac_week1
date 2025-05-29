import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n, target = map(int, input().split())
    num_list = list(map(int, input().split()))
    queue = []
    priority_list = []
    priority_max = 0
    cnt = 1
    
    for i, value in enumerate(num_list):
        priority_max = max(value, priority_max)
        queue.append((i, value))
        priority_list.append(value)
        
    priority_list.sort(reverse=True)
    if len(num_list) == 1:
        print(1)
    else:
        while queue:
            if queue[0][0] == target and queue[0][1] == priority_max :
                print(cnt)
                break
            elif priority_max > queue[0][1]:
                not_target = queue.pop(0)
                queue.append(not_target)
            elif priority_max <= queue[0][1]:
                queue.pop(0)
                priority_list.pop(0)
                priority_max = priority_list[0]
                cnt +=1
    
    
