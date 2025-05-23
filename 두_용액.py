import sys
input = int(input())
liquids = list(map(int, sys.stdin.readline().split()))
liquids.sort()

negative_num = liquids[0]
postive_num = liquids[len(liquids) - 1]
result = negative_num + postive_num
while negative_num <= postive_num:
    mid = (negative_num + postive_num) // 2 
    
    if mid > 0 :
        

# -43 -19 -4 1 6 22 30 99
# 1. 가장 중요한 것은 0에 가장 가까운 값을 찾아내는 것이다
# 2. 0에 가장 가깝다는 것은 어떻게 찾을 수 있을까
# 3. 일단 배열을 음수 배열과 양수 배열로 분할한다
# 4. 음수 배열을 모두 순회하면서 양수 배열의 값을 이진탐색으로 확인한다
# 5. 음수의 첫 번째 값인 -43를 탐색하는 시점에서는 가장 마지막에 있는 값과 더하여 result에 저장한다 result = 56
# 6. result의 절대값이 0보다 크다면, mid 값을 가져와서 더한 뒤, 기존 result와 비교한다. 이 중 최소값을 선택한다 22 선택 
# 7. result가 0보다 크고, pos가 abs(neg)보다 작다면 큰쪽을 탐색한다 start = mid + 1, end = mid - 1로 설정한 뒤 한 번 더 이분 탐색을 실시한다