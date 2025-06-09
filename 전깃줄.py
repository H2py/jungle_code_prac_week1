import sys
input = sys.stdin.readline

N = int(input())
pole = []
dp = [0] * 501
cnt = 0

for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        pole.append((abs(b-a), b,a))
    else:
        pole.append((abs(b-a),a,b))


for i in range(N):
    for j in range(pole[i][1], pole[i][2]+1):
        dp[j] += 1

max_pole = max(pole)
print(max_pole)
while max_pole[0] <= 1:
    cnt += 1
    for i in range(max_pole[1], max_pole[2]+1):
        dp[i] -= 1
    print(dp)
print(cnt)