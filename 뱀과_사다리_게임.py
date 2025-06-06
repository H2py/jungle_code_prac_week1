import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

ledgers_snakes = []
for _ in range(N):
    u,v = map(int, input().split())
    ledgers_snakes.append(('ledger', u, v))

for _ in range(M):
    u,v = map(int, input().split())
    ledgers_snakes.append(('snake', u, v))

q = deque([1])

cnt = 0
while q :
    cur_cord = q.popleft()
    
    if cur_cord == 100: 
        print(cnt)
        sys.exit()

    for next_cord in [cur_cord + 1, cur_cord + 2, cur_cord + 3, cur_cord + 4, cur_cord + 5, cur_cord + 6]:
        for type, u, v in ledgers_snakes:
            if type == 'snake':
                if next_cord == u:
                    q.append(v)
            elif type == 'ledger':
                if next_cord == u:
                    q.append(v)
            else:
                q.append(next_cord)
                    
    