import sys
input = sys.stdin.readline

N, K = map(int, input().split())
elects = list(map(int, input().split()))
used = []
cnt = 0

for i in range(K):
    cur = elects[i]
    
    if cur in used:
        continue
    
    if len(used) < N :
        used.append(cur)
        continue
    
    farthest_idx = -1
    
    for u in used:
        if u not in elects[i+1:]:
            target = u
            break
        else:
            next_idx = elects[i+1:].index(u)
            if next_idx > farthest_idx:
                farthest_idx = next_idx
                target = u
                
    used.remove(target)
    used.append(cur)
    cnt += 1
    
print(cnt)
            
        