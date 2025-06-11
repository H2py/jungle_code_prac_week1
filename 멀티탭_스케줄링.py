import sys
input = sys.stdin.readline

N, K = map(int, input().split())
elects = list(map(int, input().split()))
used = []
used_idx = [-1] * (K-N)

for _ in range(N):
    used.append(elects.pop(0))


for i in range(K-N):
    if elects[i] in used:
        used_idx[i] = used.index(elects[i]) 

    
for elect in elects:
    for i in range(N):
        if used[i] == elect:
            continue
        elif used[i] != elect and used_idx[i] == -1:
            for j in range
            
# 1 2 7을 다룰거임 근데, 이걸 2, 3을 확인하면서 언제 넣어야 적절한지를 확인해줘야하는거잖아
# 1 2 3을 기준으로 생각해보자

# 4 1 2
# 여기서 알 수 있는 것은 4 1 2의 교환이 3 1 2로 이루어져야한다는 것이다
# 그렇다면 여기서 3이라는 숫자는 어디서 도출될 수 있을까?
# 기존 순서리스트를 순회한다